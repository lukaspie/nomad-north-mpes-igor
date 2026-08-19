# Build the Image

This plugin has no published image (see [Explanation > Why Igor is never committed here](../explanation/explanation.md#why-igor-is-never-committed-here)). Building it is always a manual, local step, done by whoever holds an Igor Pro license.

## Prerequisites

- A valid Igor Pro license from [WaveMetrics](https://www.wavemetrics.com/){:target="_blank" rel="noopener"}.
- Docker.

## Steps

1. **Build a Wine-only placeholder image.** `docker build` still needs *something* at
   `igor-wine/` for `COPY` to succeed, even though Igor isn't installed yet -- an empty directory
   satisfies that:

   ```bash
   mkdir -p src/nomad_north_mpes_igor/north_tools/mpes_igor/igor-wine
   docker build -f src/nomad_north_mpes_igor/north_tools/mpes_igor/Dockerfile \
       -t nomad-north-mpes-igor:wine-only .
   ```

   The result is a real, runnable image with Wine installed and a Desktop shortcut already
   wired up (it just points at an Igor binary that doesn't exist yet).

2. **Run it and open the desktop**, the same way you'd use the finished tool later:

   ```bash
   docker run --rm -p 8888:8888 nomad-north-mpes-igor:wine-only
   ```

   Open `http://localhost:8888/desktop` in a browser -- this is the same `xfce` desktop the
   `pynxtools-mpes` NORTH tool uses, reached the same way NOMAD would reach it.

3. **Download and run the Igor Pro installer under Wine**, in a terminal inside that desktop.
   This is the actual, one-time installation step -- everything after it is just packaging what
   you're about to create here:

   ```bash
   wget https://www.wavemetrics.net/Downloads/Win/setupIgor9.exe
   wine setupIgor9.exe
   ```

   Click through the installer accepting the defaults. If Wine prompts to install Wine Mono,
   skip it -- it isn't required by Igor. If you have your own Igor Pro license key, enter it now,
   before extracting the prefix in step 5 -- otherwise you'd have to enter it again every time
   you launch the finished container.

4. **Verify it installed correctly** by launching it directly, before going through the trouble
   of extracting and rebuilding:

   ```bash
   wine ~/.wine/drive_c/Program\ Files/WaveMetrics/Igor\ Pro\ 9\ Folder/IgorBinaries_x64/Igor64.exe
   ```

5. **Extract the Wine prefix.** `docker cp` reaches into the *running* container from your host
   and copies files out of it -- this is how the Igor installation you just did inside the
   container becomes a directory `docker build` can `COPY` from on your next build. Replace the
   empty placeholder from step 1 with the real thing:

   ```bash
   docker ps  # note the container ID for nomad-north-mpes-igor:wine-only
   rm -rf src/nomad_north_mpes_igor/north_tools/mpes_igor/igor-wine
   docker cp <container_id>:/home/jovyan/.wine \
       src/nomad_north_mpes_igor/north_tools/mpes_igor/igor-wine
   ```

6. **Rebuild.** This is now an ordinary `docker build` -- no more interactive steps. `COPY` picks
   up the real, licensed Igor installation from `igor-wine/` this time, and bakes it into the
   image:

   ```bash
   docker build -f src/nomad_north_mpes_igor/north_tools/mpes_igor/Dockerfile \
       -t nomad-north-mpes-igor:latest .
   ```

## Why two passes

The [Dockerfile](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/blob/main/src/nomad_north_mpes_igor/north_tools/mpes_igor/Dockerfile){:target="_blank" rel="noopener"} `COPY`s a directory called `igor-wine/` -- a Wine prefix with Igor Pro already installed inside it -- straight into the image. Docker's `COPY` has no interactive installer step of its own: it only copies files that already exist on your machine before the build starts. So the Igor installation itself can't happen *during* `docker build` the way the WineHQ apt install does -- it has to happen first, in a real running container, the normal way you'd install any Windows program under Wine (double-click the installer, click through it). Only once that's done is
there anything for `COPY` to pick up. That's what steps 1-5 do: build a container that has Wine but not yet Igor, run it, install Igor inside it like you would on a normal Linux+Wine desktop, then copy the resulting `~/.wine` directory back out to your host so it can become the `igor-wine/` input the real
`COPY` step needs. Step 6 is then an entirely ordinary rebuild.

## Using the image

A local tag is enough to try this out -- NOMAD checks for a local image before pulling from a
registry, so nothing needs to be pushed anywhere yet. See
[How-to guides > Install this Plugin](install_this_plugin.md) for how to point a running NOMAD
at the tag you just built.

Only push `nomad-north-mpes-igor:latest` to a registry (e.g. an oasis-local one -- there is no
FAIRmat-published image) if you need the image on a machine other than the one you built it on.

## Further notes

- To add a default template, procedure files, or similar, mount them into Igor's `User
  Procedures` folder inside the Wine prefix, or modify the startup wiring
  (`config/autostart`/`config/Igor.desktop`) before rebuilding.
- Steps 1-5 only need to be repeated when the Igor installation itself needs to change (a new
  Igor version, a different license). Routine rebuilds of the Dockerfile (picking up Wine
  version bumps, config changes, etc.) can reuse the same `igor-wine/` prefix as-is -- just
  re-run step 6.
