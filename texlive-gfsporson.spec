# revision 18651
# category Package
# catalog-ctan /fonts/greek/gfs/gfsporson
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license other-free
# catalog-version 1.01
Name:		texlive-gfsporson
Version:	1.01
Release:	5
Summary:	A Greek font, originally from Porson
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfsporson
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsporson.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsporson.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Porson is an elegant Greek font, originally cut at the turn of
the 19th Century in England. The present version has been
provided by the Greek Font Society. The font supports the Greek
alphabet only. LaTeX support is provided, using the LGR
encoding.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfsporson/GFSPorson-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsporson/porsonel.enc
%{_texmfdistdir}/fonts/map/dvips/gfsporson/gfsporson.map
%{_texmfdistdir}/fonts/opentype/public/gfsporson/GFSPorson.otf
%{_texmfdistdir}/fonts/tfm/public/gfsporson/gporsonrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsporson/gporsonrg6r.tfm
%{_texmfdistdir}/fonts/type1/public/gfsporson/GFSPorson-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsporson/gporsonrg6a.vf
%{_texmfdistdir}/tex/latex/gfsporson/gfsporson.sty
%{_texmfdistdir}/tex/latex/gfsporson/lgrporson.fd
%doc %{_texmfdistdir}/doc/fonts/gfsporson/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfsporson/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfsporson/README
%doc %{_texmfdistdir}/doc/fonts/gfsporson/gfsporson.pdf
%doc %{_texmfdistdir}/doc/fonts/gfsporson/gfsporson.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 752311
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 718552
- texlive-gfsporson
- texlive-gfsporson
- texlive-gfsporson
- texlive-gfsporson

