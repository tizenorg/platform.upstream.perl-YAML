# This spec file originally comes from openSUSE, with copyright notice below:
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An &quot;Open Source License&quot; is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           perl-YAML
Version:        0.84
Release:        0
License:        GPL-2.0+ or Artistic-1.0
%define cpan_name YAML
Summary:        YAML Ain't Markup Language (tm)
Url:            http://search.cpan.org/dist/YAML/
Group:          Development/Libraries/Perl
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildArch:      noarch

%description
The YAML.pm module implements a YAML Loader and Dumper based on the YAML
1.0 specification. the http://www.yaml.org/spec/ manpage

YAML is a generic data serialization language that is optimized for human
readability. It can be used to express the data structures of most modern
programming languages. (Including Perl!!!)

For information on the YAML syntax, please refer to the YAML specification.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
