# SPDX-FileCopyrightText: The nomad-north-mpes-igor Authors
#
# This file is part of nomad-north-mpes-igor.
#
# SPDX-License-Identifier: MIT

ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/pynxtools-mpes

FROM ${BASE_IMAGE}:${IMAGE_TAG}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# ---- Wine (generic — the same steps apply to any Windows-only NORTH tool overlay, e.g. a
# future CasaXPS overlay for pynxtools-xps; keep this block in sync if copied elsewhere) ----
RUN dpkg --add-architecture i386 \
 && mkdir -pm755 /etc/apt/keyrings \
 && wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key \
 && wget -nc -P /etc/apt/sources.list.d/ \
      https://dl.winehq.org/wine-builds/ubuntu/dists/$(lsb_release -sc)/winehq-$(lsb_release -sc).sources \
 && apt-get update -y \
 && apt-get install -y --install-recommends winehq-staging \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Wine prompts interactively to download Wine Mono (needed by some .NET-based
# installers/apps) the first time it's needed - there's no GUI to click through
# in a Dockerfile or a headless container, so it has to be pre-placed instead.
# Version must be kept roughly in step with the wine-staging version installed
# above; check https://dl.winehq.org/wine/wine-mono/ if this ever needs bumping.
ARG WINE_MONO_VERSION=11.3.0
RUN mkdir -p /usr/share/wine/mono \
 && wget -q -O /tmp/wine-mono.tar.xz \
      https://dl.winehq.org/wine/wine-mono/${WINE_MONO_VERSION}/wine-mono-${WINE_MONO_VERSION}-x86.tar.xz \
 && tar -xf /tmp/wine-mono.tar.xz -C /usr/share/wine/mono \
 && rm /tmp/wine-mono.tar.xz

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
WORKDIR "${HOME}"

# ---- Igor Pro (proprietary — never committed) ----
# Requires a locally-supplied, licensed Igor Wine prefix at build time. Place it at
# src/nomad_north_mpes_igor/north_tools/mpes_igor/igor_wine (gitignored) before running
# `docker build`. See this package's README for how to produce that prefix.
# COPY paths are relative to the build context root (package root), not this Dockerfile's
# own directory — matching the convention used in pynxtools-mpes's own Dockerfile.
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/igor_wine "${HOME}/.wine"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/config/Igor.desktop "${HOME}/Desktop/Igor.desktop"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/config/Igor64.ico "${HOME}/Igor64.ico"
# Uses filenames distinct from nomad-north-desktop-base's own autostart.desktop/
# autostart (the generic Desktop-icon trust-marking entry) - COPYing to the same
# destination would silently overwrite that base entry instead of adding to it,
# leaving every non-Igor icon (Chrome, silx, VS Code, ...) untrusted.
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/config/igor-workdir-setup.desktop "${HOME}/.config/autostart/igor-workdir-setup.desktop"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/config/igor-workdir-setup "${HOME}/.config/autostart/igor-workdir-setup"
RUN chmod 755 "${HOME}/Desktop/Igor.desktop" \
    "${HOME}/.config/autostart/igor-workdir-setup.desktop" \
    "${HOME}/.config/autostart/igor-workdir-setup"

WORKDIR "${HOME}"

EXPOSE 8888
