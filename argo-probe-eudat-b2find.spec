Name:		argo-probe-eudat-b2find
Version:	2.5
Release:	3%{?dist}
Summary:	B2FIND metrics to check the functionality of the service. 
License:	GPLv3+
Packager:	Heinrich Widmann <widmann@dkrz.de>
Group:		Application
URL:		http://b2find.eudat.eu/
Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}


#BuildRequires:	
Requires:	python
Requires:	python-argparse
#Requires:	python-json
#Requires:	python-urllib
#Requires:	python-urllib2

%description
This plugin provides the nessecary script to check search functionality of the B2FIND discovery service b2find.eudat.eu .

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

install -d %{buildroot}/%{_sysconfdir}/argo/probes/eudat-b2find
install -m 755 checkB2FIND.py %{buildroot}/%{_libexecdir}/argo/probes/eudat-b2find/checkB2FIND.py

%files
%dir /%{_libexecdir}/argo
%dir /%{_libexecdir}/argo/probes/
%dir /%{_libexecdir}/argo/probes/eudat-b2find

%attr(0755,root,root) /%{_libexecdir}/argo/probes/eudat-b2find/checkB2FIND.py

%pre

%changelog
* Fri Mar 04 2022 Themis Zamani <themis@admin.grnet.gr> - 2.5-3
* Fri Mar 26 2021 Themis Zamani <themis@admin.grnet.gr> - 2.4-1
* Wed Mar 24 2021 Themis Zamani <themis@admin.grnet.gr> - 2.2-1
- Add rpm dependencies
* Tue Mar 07 2017  Heinrich Widmann <widmann@dkrz.de> 0.1
- Initial version of b2find nagios plugin
