Name:		cronexec
Version:	0.90
Release:	1%{?dist}
Summary:	cronexec executes a command for every specified second interval. 

Group:		System Environment/Base
License:	GPLv2
URL:		http://www.netfort.gr.jp/~tosihisa/cronexec
Source0:	http://www.netfort.gr.jp/~tosihisa/cronexec/cronexec-0.90.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
cronexec executes a command for every specified second interval.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install PREFIX=%{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/cronexec
%{_bindir}/schedexec
