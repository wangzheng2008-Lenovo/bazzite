Name:          usbhid-gadget-passthru
Summary:       SteamOS USB passthrough support

Version:       {{{ git_dir_version }}}
Release:       1%{?dist}
License:       BSD-3-Clause

URL:           https://gitlab.com/evlaV/%{name}
Source:        %{url}/-/archive/main/%{name}-main.tar.gz

BuildRequires: gcc

%description
SteamOS USB passthrough support

%prep
%autosetup -p1 -n %{name}-main

%build
%make

%install
mkdir -p %{_buildroot}/%{_bindir}
install -Ds -m755 -t %{_buildroot}/usr/bin usbhid-gadget-passthru

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
