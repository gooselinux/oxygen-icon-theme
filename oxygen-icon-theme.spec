
Name:          oxygen-icon-theme 
Summary:       Oxygen icon theme 
Version:       4.3.4
Release:       2%{?dist}

License:       LGPLv3+ 
Group:         User Interface/Desktops
URL:           http://www.kde.org/
Source0:       ftp://ftp.kde.org/pub/kde/stable/%{version}/src/oxygen-icons-%{version}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:     noarch

BuildRequires: cmake
BuildRequires: kde-filesystem

Obsoletes: oxygen-icon-theme-scalable < 4.2.85 


%description
%{summary}.


%prep
%setup -q -n oxygen-icons-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform} 


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%post 
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :

%posttrans 
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :

%postun 
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
fi


%files 
%defattr(-,root,root,-)
%doc AUTHORS CONTRIBUTING COPYING TODO*
%{_kde4_iconsdir}/oxygen/


%changelog
* Fri Jan 01 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.4-2
- Related: rhbz#543948 (fix upstream URL)

* Tue Dec 01 2009 Than Ngo <than@redhat.com> - 4.3.4-1
- 4.3.4

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Mon Jul 13 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Fri Jun 26 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Fri May 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.85-1
- oxygen-icons-4.2.85

* Tue Mar 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-1
- kde-4.2.2

* Mon Mar 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-11
- License: LGPLv3+
- %%doc: AUTHORS CONTRIBUTING COPYING TODO*

* Fri Mar 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-10
- standalone (noarch) oxygen-icon-theme

