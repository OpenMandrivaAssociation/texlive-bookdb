Name:		texlive-bookdb
Version:	37536
Release:	2
Summary:	A BibTeX style file for cataloguing a home library
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bookdb
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookdb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookdb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an extended book entry for use in
cataloguing a home library. The extensions include fields for
binding, category, collator, condition, copy, illustrations,
introduction, location, pages, size, value, volumes.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/bookdb
%doc %{_texmfdistdir}/doc/bibtex/bookdb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
