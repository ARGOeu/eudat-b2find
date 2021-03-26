Name:		eudat-b2find
Version:	2.2
Release:	1%{?dist}
Summary:	Nagios B2FIND probes
License:	GPLv3+
Packager:	Heinrich Widmann <widmann@dkrz.de>
Group:		Application
URL:		http://www.eudat.eu/b2find

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
This nagios plugin provides the nessecary script to check search functionality of the B2FIND discovery service b2find.eudat.eu .

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-b2find
install -d %{buildroot}/%{_sysconfdir}/nagios/plugins/eudat-b2find
install -m 755 checkB2FIND.py %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-b2find/checkB2FIND.py

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/eudat-b2find
%dir /%{_sysconfdir}/nagios/plugins/eudat-b2find

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/eudat-b2find/checkB2FIND.py
%attr(0755,root,root) /%{_sysconfdir}/nagios/plugins/eudat-b2find

%post
%changelog
* Tue Mar 07 2017  Heinrich Widmann <widmann@dkrz.de> 0.1
- Initial version of b2find nagios plugin
