Name:           procenv
Version:        0.51
Release:        1
Summary:        Utility to show process environment
License:        GPLv3+
URL:            https://github.com/jamesodhunt/procenv
Source0:        https://github.com/jamesodhunt/procenv/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libselinux)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(expat)
# Only used for testing; not in EPEL.
BuildRequires:  perl(JSON::PP)
%ifnarch %{armx} %{riscv} s390 s390x
BuildRequires:  pkgconfig(numa)
%endif

%description
This package contains a command-line tool that displays as much
detail about itself and its environment as possible. It can be
used as a test tool, to understand the type of environment a
process runs in, and for comparing system environments.

%prep
%setup -q
# remove symlink
mv README.rst README

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%{_bindir}/procenv
%{_mandir}/man1/procenv.1*
# ChangeLog is empty
%doc README NEWS AUTHORS TODO
%license COPYING
