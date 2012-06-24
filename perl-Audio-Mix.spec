#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Mix
Summary:	Audio::Mix Perl module - Wav/CoolEdit Fader/Cross-Fader
Summary(pl):	Modu� Perla Audio::Mix - dodaj�cy wyciszenia lub przej�cia do pr�bek wav
Name:		perl-Audio-Mix
Version:	0.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-cue.patch
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Audio-Tools
BuildRequires:	perl-Audio-Wav
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional, fake
%define		_noautoreq	'perl(Audio::CoolEdit)' 'perl(join)'

%description
The purpose of this module is to provide a way to apply fades to
uncompressed Microsoft .wav files. Not being a c programmer, the fades
are done completely in Perl, making a minutes fade on a stereo 44.1
Khz, 16bit file take a considerable amount of time. The primary reason
I wrote this module was because I needed a programmatic way to mix
songs together for subsequent burning to a CDR.

%description -l pl
Celem tego modu�u jest udost�pnienie sposobu na dodawanie wycisze� lub
p�ynnych przej�� do nieskompresowanych plik�w .wav. Efekty te s�
wykonywane ca�kowicie w Perlu, wi�c dodawanie wyciszenia do 16-bitowej
pr�bki stereo 44.1kHz mo�e troch� potrwa�. G��wnym powodem stworzenia
tego modu�u by�a programowego miksowania utwor�w w celu nagrywania na
CDR.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Audio/Mix.pm
%{perl_sitelib}/Audio/Mix
%{_mandir}/man3/*
