#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Mix
Summary:	Audio::Mix Perl module - Wav/CoolEdit Fader/Cross-Fader
Summary(pl.UTF-8):	Moduł Perla Audio::Mix - dodający wyciszenia lub przejścia do próbek WAV
Name:		perl-Audio-Mix
Version:	0.01
Release:	5
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	795c50919e094e3472d53993aa39fe50
Patch0:		%{name}-cue.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Audio-Tools
BuildRequires:	perl-Audio-Wav
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional, fake
%define		_noautoreq	'perl(Audio::CoolEdit)' 'perl(join)'

%description
The purpose of this module is to provide a way to apply fades to
uncompressed Microsoft .WAV files. Not being a c programmer, the fades
are done completely in Perl, making a minutes fade on a stereo 44.1
Khz, 16bit file take a considerable amount of time. The primary reason
I wrote this module was because I needed a programmatic way to mix
songs together for subsequent burning to a CDR.

%description -l pl.UTF-8
Celem tego modułu jest udostępnienie sposobu na dodawanie wyciszeń lub
płynnych przejść do nieskompresowanych plików .WAV. Efekty te są
wykonywane całkowicie w Perlu, więc dodawanie wyciszenia do 16-bitowej
próbki stereo 44.1kHz może trochę potrwać. Głównym powodem stworzenia
tego modułu była programowego miksowania utworów w celu nagrywania na
CDR.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Audio/Mix.pm
%{perl_vendorlib}/Audio/Mix
%{_mandir}/man3/*
