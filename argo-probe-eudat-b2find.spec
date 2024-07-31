Name:		argo-probe-eudat-b2find
Version:	2.9
Release:	1%{?dist}
Summary:	B2FIND metrics to check the functionality of the service.
License:	GPLv3+
Packager:	Heinrich Widmann <widmann@dkrz.de>
Group:		Application
URL:		http://b2find.eudat.eu/
Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}


#BuildRequires:
Requires:	python3
Requires:	python3-requests

%description
This plugin provides the nessecary script to check search functionality of the B2FIND discovery service b2find.eudat.eu .

%prep
%setup -q

%define _unpackaged_files_terminate_build 0

install -d %{buildroot}/%{_libexecdir}/argo/probes/eudat-b2find
install -m 755 checkB2FIND.py %{buildroot}/%{_libexecdir}/argo/probes/eudat-b2find/checkB2FIND.py

%files
%dir /%{_libexecdir}/argo
%dir /%{_libexecdir}/argo/probes/
%dir /%{_libexecdir}/argo/probes/eudat-b2find

%attr(0755,root,root) /%{_libexecdir}/argo/probes/eudat-b2find/checkB2FIND.py

%pre

%changelog
* Fri Jul 31 2024 Themis Zamani <themis@admin.grnet.gr> - 2.9-1
- Update/upgrade to python3 for Rocky9
* Fri May 05 2023 Themis Zamani <themis@admin.grnet.gr> - 2.8-1
- AO-790 Metrics b2find - showGroupEnes produces an UNKNOWN state
* Thu Sep 22 2022 Katarina Zailac <kzailac@srce.hr> - 2.7-1
- ARGO-3992 Fix how checkB2FIND.py probe handles timeout
* Fri Jun 22 2022 Themis Zamani <themis@admin.grnet.gr> - 2.6-1
* Fri Mar 04 2022 Themis Zamani <themis@admin.grnet.gr> - 2.5-3
* Fri Mar 26 2021 Themis Zamani <themis@admin.grnet.gr> - 2.4-1
* Wed Mar 24 2021 Themis Zamani <themis@admin.grnet.gr> - 2.2-1
- Add rpm dependencies
* Tue Mar 07 2017  Heinrich Widmann <widmann@dkrz.de> 0.1
- Initial version of b2find nagios plugin
