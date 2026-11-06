FROM mcr.microsoft.com/devcontainers/cpp:3-debian13

ARG REINSTALL_CMAKE_VERSION_FROM_SOURCE="3.22.2"

# Optionally install the cmake for vcpkg
COPY ./reinstall-cmake.sh /tmp/

RUN if [ "${REINSTALL_CMAKE_VERSION_FROM_SOURCE}" != "none" ]; then \
        chmod +x /tmp/reinstall-cmake.sh && /tmp/reinstall-cmake.sh ${REINSTALL_CMAKE_VERSION_FROM_SOURCE}; \
    fi \
    && rm -f /tmp/reinstall-cmake.sh

# [Optional] Uncomment this section to install additional vcpkg ports.
# RUN su vscode -c "${VCPKG_ROOT}/vcpkg install <your-port-name-here>"

# Dépôts Debian en HTTPS (le HTTP simple est bloqué sur certains réseaux)
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list.d/debian.sources

# [Optional] Uncomment this section to install additional packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3-pybind11 pybind11-dev python3-tk python3-venv \
    python3-pip \
    zstd \
    fonts-noto-color-emoji fonts-noto-core fonts-dejavu-core fonts-noto-extra

# customtkinter pour l'interface graphique Python
RUN pip3 install --break-system-packages customtkinter

# opencode (assistant de code), installé pour l'utilisateur vscode
# Ollama tourne sur Windows et est joint via host.docker.internal (voir opencode.json)
RUN su vscode -c "curl -fsSL https://opencode.ai/install | bash" \
    && ln -s /home/vscode/.opencode/bin/opencode /usr/local/bin/opencode
