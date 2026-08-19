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

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
WORKDIR "${HOME}"

# ---- Igor Pro (proprietary — never committed) ----
# Requires a locally-supplied, licensed Igor Wine prefix at build time. Place it at
# src/nomad_north_mpes_igor/north_tools/mpes_igor/igor-wine (gitignored) before running
# `docker build`. See this package's README for how to produce that prefix.
# COPY paths are relative to the build context root (package root), not this Dockerfile's
# own directory — matching the convention used in pynxtools-mpes's own Dockerfile.
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/igor-wine "${HOME}/.wine"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/config/Igor.desktop "${HOME}/Desktop/Igor.desktop"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/config/Igor64.ico "${HOME}/Igor64.ico"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/config/autostart.desktop "${HOME}/.config/autostart/autostart.desktop"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_mpes_igor/north_tools/mpes_igor/config/autostart "${HOME}/.config/autostart/autostart"
RUN chmod 755 "${HOME}/Desktop/Igor.desktop" \
    "${HOME}/.config/autostart/autostart.desktop" \
    "${HOME}/.config/autostart/autostart"

WORKDIR "${HOME}"

EXPOSE 8888
