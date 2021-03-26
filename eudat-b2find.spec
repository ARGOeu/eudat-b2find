Name:		eudat-b2find
Version:	2.2
Release:	0
Summary:	Nagios B2FIND probes
License:	GPLv3+
Packager:	Heinrich Widmann <widmann@dkrz.de>

Group:		Application
URL:		http://www.eudat.eu/b2find
BuildArch:	noarch
#Source0:	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
Requires:	python
Requires:	python-argparse
#Requires:	python-json
#Requires:	python-urllib
#Requires:	python-urllib2

%description
This nagios plugin provides the nessecary script to check search functionality of the B2FIND discovery service b2find.eudat.eu .

%define _whoami %(whoami)
%define _b2findhomepackaging %(pwd)
%define _b2findNagiosPackage /usr/libexec/argo-monitoring/probes/eudat-b2find

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

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/eudat-b2find/checkB2FIND.py

%post
%changelog
* Tue Mar 07 2017  Heinrich Widmann <widmann@dkrz.de> 0.1
- Initial version of b2find nagios plugin
