Summary:	GD perl module
Summary(pl):	Modu³ perla GD
Name:		perl-GD
Version:	1.19
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GD-%{version}.tar.gz
Patch:		perl-GD-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GD - Interface to Gd Graphics Library.

%description -l pl
GD - interfejs do biblioteki Gd.

%prep
%setup -q -n GD-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install {demos/*,bdftogd,fonttest} \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/GD/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/GD
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README*}.gz

%{perl_sitearch}/GD.pm
%{perl_sitearch}/qd.pl
%{perl_sitearch}/auto/libgd

%dir %{perl_sitearch}/auto/GD
%{perl_sitearch}/auto/GD/.packlist
%{perl_sitearch}/auto/GD/autosplit.ix
%{perl_sitearch}/auto/GD/GD.bs
%attr(755,root,root) %{perl_sitearch}/auto/GD/GD.so

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
