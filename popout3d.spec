Name:           popout3d
Version:        1.6.44
Release:        1%{?dist}
Summary:        Pop-out 3D image viewer

License:        GPL-3.0-or-later
URL:            https://github.com/PopoutApps/popout3d
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
Requires:       python3
Requires:       hugin

%description
Pop-out 3D lets you create anaglyph and stereoscopic images. Requires align_image_stack (from hugin-tools) for automatic image alignment.

%global debug_package %{nil}

%prep
%setup -q

%build
# No C compilation; only Python and data files

%install
rm -rf %{buildroot}
meson setup builddir --prefix=%{_prefix}
meson install -C builddir --destdir=%{buildroot}

%files
%license LICENSE
%{_bindir}/popout3d
%{_datadir}/popout3d
%{_datadir}/applications/popout3d.desktop
%{_datadir}/metainfo/popout3d.metainfo.xml
%{_datadir}/icons/hicolor/64x64/apps/popout3d.png
%{_datadir}/icons/hicolor/128x128/apps/popout3d.png
%{_datadir}/locale/nl/LC_MESSAGES/popout3d.mo
%{_datadir}/locale/de/LC_MESSAGES/popout3d.mo
%{_datadir}/locale/es/LC_MESSAGES/popout3d.mo
%{_datadir}/locale/fr/LC_MESSAGES/popout3d.mo

%changelog
* Sun Feb 8 2026 Chris <chris@example.com> - 1.6.44-1
- Initial RPM packaging

