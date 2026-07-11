%global tl_name gfsporson
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	A Greek font, originally from Porson
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsporson
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsporson.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsporson.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Porson is an elegant Greek font, originally cut at the turn of the 19th
Century in England. The present version has been provided by the Greek
Font Society. The font supports the Greek alphabet only. LaTeX support
is provided, using the LGR encoding.

