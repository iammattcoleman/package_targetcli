%global oname targetcli-fb

Name:           targetcli
License:        AGPLv3
Group:          System Environment/Libraries
Summary:        An administration shell for storage targets
Version:        2.0rc1.fb18
Release:        1%{?dist}
URL:            https://github.com/agrover/targetcli-fb
# Acquire with
# wget --content-disposition https://github.com/agrover/%{oname}/archive/v%{version}.tar.gz
# and it will save with the name below. Not cool, github.
Source:         https://github.com/agrover/%{oname}/archive/%{oname}-%{version}.tar.gz
Source1:        targetcli.service
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel python-rtslib python-configshell epydoc
BuildRequires:  systemd-units
Requires:       python-rtslib >= 2.1.fb26, python-configshell, python-ethtool
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.


%prep
%setup -q -n %{oname}-%{version}

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
%systemd_post targetcli.service

%preun
%systemd_preun targetcli.service

%postun
%systemd_postun_with_restart targetcli.service

%files
%defattr(-,root,root,-)
%{python_sitelib}/*
%{_bindir}/targetcli
%{_unitdir}/targetcli.service
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup
%doc COPYING README
%{_mandir}/man8/targetcli.8.gz

%changelog
* Thu Dec 20 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 2.0rc1.fb18-1
- New upstream release
- Add python-ethtool requires
- Update Source0 to use Github tar-from-tag instead of Downloads

* Thu Dec 13 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 2.0rc1.fb17-2
- Scriptlets replaced with new systemd macros (#850335)

* Mon Nov 12 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb17-1
- New upstream release

* Tue Aug 7 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb16-1
- New upstream release
- Update rtslib version dependency

* Tue Jul 31 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb15-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0rc1.fb14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb14-2
- Fix %files to claim /etc/target, not claim sitelib

* Thu Jun 28 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb14-1
- New upstream release

* Tue Jun 12 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb13-1
- New upstream release

* Wed May 30 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb12-1
- Update Source URL to proper tarball
- New upstream release

* Mon Apr 9 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb11-1
- New upstream release

* Wed Feb 29 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb10-1
- New upstream release

* Tue Feb 21 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb9-1
- New upstream release

* Thu Feb 16 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb8-1
- New upstream release

* Wed Feb 8 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb7-1
- New upstream release

* Fri Feb 3 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb6-1
- New upstream release

* Tue Jan 24 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb5-2
- Update After= in service file to wait for localfs and network
- Improve description in service file

* Tue Jan 24 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb5-1
- New upstream release

* Fri Jan 13 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb4-1
- New upstream release

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb3-2
- Fix service file to mount configfs before starting targetcli

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb3-1
- New upstream release
- Fixup service file for new start/stop targetcli commands

* Tue Dec 6 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb2-1
- New upstream source and release
- Remove patches:
  * targetcli-git-version.patch
  * 0001-Remove-ads-from-cli-welcome-msg.-Mention-help-is-ava.patch
  * 0002-bundle-lio-utils.patch
  * 0003-Hack.-dump-scripts-aren-t-in-PATH-anymore-so-call-th.patch
  * 0004-ignore-errors-from-failure-to-set-device-attributes.patch
  * 0005-fix-spec_root-path.patch
  * 0006-add-docs.patch
  * 0007-all-start.patch

* Mon Nov 21 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-4
- Update doc patch to include iscsi tutorial

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
