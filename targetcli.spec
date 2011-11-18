Name:           targetcli
License:        AGPLv3
Group:          System Environment/Libraries
Summary:        An administration shell for storage targets
Version:        1.99.2.gitb03ec79
Release:        3%{?dist}
# placeholder URL and source entries
# archive created using:
# git clone git://risingtidesystems.com/targetcli.git
# cd targetcli
# git archive b03ec79 --prefix targetcli-%{version}/ | gzip > targetcli-%{version}.tar.gz
URL:            http://www.risingtidesystems.com/git/
Source:         %{name}-%{version}.tar.gz
Source1:        targetcli.service
Patch1:         targetcli-git-version.patch
Patch2:         0001-Remove-ads-from-cli-welcome-msg.-Mention-help-is-ava.patch
Patch3:         0002-bundle-lio-utils.patch
Patch4:         0003-Hack.-dump-scripts-aren-t-in-PATH-anymore-so-call-th.patch
Patch5:         0004-ignore-errors-from-failure-to-set-device-attributes.patch
Patch6:         0005-fix-spec_root-path.patch
Patch7:         0006-add-docs.patch
Patch8:         0007-all-start.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel python-rtslib python-configshell epydoc
BuildRequires:  systemd-units
Requires:       python-rtslib python-configshell
Requires(post): systemd-units


%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.


%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%{__python} setup.py build
gzip --stdout targetcli.8 > targetcli.8.gz

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/targetcli.service
install -m 644 targetcli.8.gz %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%post
if [ $1 -eq 1 ] ; then 
    # Initial installation
    /bin/systemctl enable targetcli.service >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%{python_sitelib}
%{_bindir}/targetcli
%{_unitdir}/targetcli.service
%dir %{_sysconfdir}/target/backup
%doc COPYING README
%{_mandir}/man8/targetcli.8.gz

%changelog
* Wed Nov 2 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-3
- Add buildrequires for systemd-units
- use _unitdir
- remove preun, modify post

* Wed Nov 2 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-2
- Add patch
  * 0007-all-start.patch
- Replace sysv init with systemd init

* Fri Oct 7 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-1
- Initial Fedora packaging
