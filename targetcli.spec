%global oname targetcli-fb

Name:           targetcli
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        An administration shell for storage targets
Version:        2.1.fb35
Release:        1%{?dist}
URL:            https://fedorahosted.org/targetcli-fb/
Source:         https://fedorahosted.org/released/targetcli-fb/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-rtslib >= 2.1.fb41, python-configshell >= 2.1.fb12, python-ethtool


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
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 targetcli.8.gz %{buildroot}%{_mandir}/man8/

%files
%{python_sitelib}/*
%{_bindir}/targetcli
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup
%doc COPYING README.md
%{_mandir}/man8/targetcli.8.gz

%changelog
* Fri Mar 14 2014 Andy Grover <agrover@redhat.com> - 2.1.fb35-1
- New upstream version

* Mon Feb 24 2014 Andy Grover <agrover@redhat.com> - 2.1.fb34-1
- New upstream version

* Wed Dec 4 2013 Andy Grover <agrover@redhat.com> - 2.1.fb33-1
- New upstream version

* Fri Nov 1 2013 Andy Grover <agrover@redhat.com> - 2.1.fb31-1
- New upstream version
- Move service handling to python-rtslib
- Remove old packaging bits: clean, buildroot, defattr

* Thu Sep 12 2013 Andy Grover <agrover@redhat.com> - 2.1.fb30-1
- New upstream version

* Tue Sep 10 2013 Andy Grover <agrover@redhat.com> - 2.1.fb29-1
- New upstream release
- Remove no-longer-needed BuildRequires

* Mon Aug 5 2013 Andy Grover <agrover@redhat.com> - 2.1.fb28-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.fb27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Andy Grover <agrover@redhat.com> - 2.1.fb27-1
- New upstream release
- License now Apache 2.0
- Remove patch modules-not-loaded.patch

* Tue Jun 18 2013 Andy Grover <agrover@redhat.com> - 2.1.fb26-2
- Add patch
  * modules-not-loaded.patch

* Fri Jun 7 2013 Andy Grover <agrover@redhat.com> - 2.1.fb26-1
- New upstream release

* Thu May 9 2013 Andy Grover <agrover@redhat.com> - 2.1.fb25-1
- New upstream release

* Thu May 2 2013 Andy Grover <agrover@redhat.com> - 2.1.fb24-1
- New upstream release
- Update source URL

* Fri Apr 12 2013 Andy Grover <agrover@redhat.com> - 2.1.fb23-1
- New upstream release

* Wed Apr 10 2013 Andy Grover <agrover@redhat.com> - 2.1.fb22-1
- New upstream release

* Mon Mar 4 2013 Andy Grover <agrover@redhat.com> - 2.0.fb21-1
- New upstream release

* Tue Feb 26 2013 Andy Grover <agrover@redhat.com> - 2.0.fb20-1
- New upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0rc1.fb19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 7 2013 Andy Grover <agrover@redhat.com> - 2.0rc1.fb19-1
- New upstream release

* Thu Jan 3 2013 Andy Grover <agrover@redhat.com> - 2.0rc1.fb18-2
- Add python-ethtool BuildRequires

* Thu Dec 20 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb18-1
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
