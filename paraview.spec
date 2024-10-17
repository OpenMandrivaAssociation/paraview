# default to enable (and build only) mpi
%bcond_without			mpi

%define namever			paraview-3.12

%define _disable_ld_no_undefined	1

%define qt_dir			%{qt4dir}
%define qt_designer_plugins_dir	%{qt4plugins}/designer
%define python_include_path	%{_includedir}/python%{pyver}
%define python_library		%{_libdir}/python%{pyver}/config/libpython%{pyver}.so

Name:		paraview
Version:	3.12.0
Release:	%mkrel 1
Summary:	Parallel visualization application
Group:		Sciences/Other
License:	BSD
URL:		https://www.paraview.org/
Source0:	http://www.paraview.org/files/v%{version}/ParaView-%{version}.tar.gz
Source1:	http://paraview.org/files/v%{version}/ParaViewData-%{version}.zip
Source2:	paraview.xml
Source3:	http://public.kitware.com/pub/paraview/logos/ParaView-logo-swirl-high-res.png
Patch0: 	paraview-3.12.0-link.patch
#Add some needed includes
Patch1: 	paraview-3.12.0-include.patch
#Reported upstream: http://public.kitware.com/mantis/view.php?id=7023
Patch2: 	paraview-3.12.0-hdf5.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	cmake
%if %{with mpi}
BuildRequires:	openmpi
BuildRequires:	openmpi-devel
%rename 	paraview-mpi
%endif
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	gnuplot
BuildRequires:	wget
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	GL-devel
BuildRequires:	libxt-devel
BuildRequires:	graphviz
BuildRequires:	hdf5-devel
BuildRequires:	imagemagick
BuildRequires:	libtiff-devel
BuildRequires:	python-devel
BuildRequires:	qt4-devel
BuildRequires:	qt4-assistant
BuildRequires:	readline-devel
BuildRequires:	tk-devel
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
Requires:	qt-assistant-adp
Requires:	qt4-database-plugin-sqlite
%ifarch %x86_64
Requires:	lib64hdf5_0
%endif
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description
ParaView is an application designed with the need to visualize large
data sets in mind. The goals of the ParaView project include the
following:

    * Develop an open-source, multi-platform visualization
      application.

    * Support distributed computation models to process large data
      sets.

    * Create an open, flexible, and intuitive user interface.

    * Develop an extensible architecture based on open standards.

ParaView runs on distributed and shared memory parallel as well as
single processor systems. Under the hood, ParaView uses the
Visualization Toolkit as the data processing and rendering engine and
has a user interface written using a unique blend of Tcl/Tk and C++.

NOTE: This version has NOT been compiled with MPI support.

%files
%defattr(-,root,root,-)
%doc License_v1.2.txt
%{_sysconfdir}/ld.so.conf.d/paraview-%{_arch}.conf
%{_bindir}/paraview
%{_bindir}/pvbatch
%{_bindir}/pvblot
%{_bindir}/pvdataserver
%{_bindir}/pvpython
%{_bindir}/pvrenderserver
%{_bindir}/pvserver
%{_bindir}/smTestDriver
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{namever}
%{_libdir}/paraview
%{py_platsitedir}/paraview.pth
%exclude %{_libdir}/%{namever}/*.cmake
%exclude %{_libdir}/%{namever}/libCosmo.so
%exclude %{_libdir}/%{namever}/libMapReduceMPI.so
%exclude %{_libdir}/%{namever}/libQVTK.so
%exclude %{_libdir}/%{namever}/libVPIC.so
%exclude %{_libdir}/%{namever}/libvtkalglib.so
%exclude %{_libdir}/%{namever}/libvtkChartsPythonD.so
%exclude %{_libdir}/%{namever}/libvtkCharts.so
%exclude %{_libdir}/%{namever}/libvtkCommonPythonD.so
%exclude %{_libdir}/%{namever}/libvtkCommon.so
%exclude %{_libdir}/%{namever}/libvtkDICOMParser.so
%exclude %{_libdir}/%{namever}/libvtkexoIIc.so
%exclude %{_libdir}/%{namever}/libvtkFilteringPythonD.so
%exclude %{_libdir}/%{namever}/libvtkFiltering.so
%exclude %{_libdir}/%{namever}/libvtkftgl.so
%exclude %{_libdir}/%{namever}/libvtkGenericFilteringPythonD.so
%exclude %{_libdir}/%{namever}/libvtkGenericFiltering.so
%exclude %{_libdir}/%{namever}/libvtkGeovisPythonD.so
%exclude %{_libdir}/%{namever}/libvtkGeovis.so
%exclude %{_libdir}/%{namever}/libvtkGraphicsPythonD.so
%exclude %{_libdir}/%{namever}/libvtkHybridPythonD.so
%exclude %{_libdir}/%{namever}/libvtkHybrid.so
%exclude %{_libdir}/%{namever}/libvtkImagingPythonD.so
%exclude %{_libdir}/%{namever}/libvtkImaging.so
%exclude %{_libdir}/%{namever}/libvtkInfovisPythonD.so
%exclude %{_libdir}/%{namever}/libvtkInfovis.so
%exclude %{_libdir}/%{namever}/libvtkIOPythonD.so
%exclude %{_libdir}/%{namever}/libvtkIO.so
%exclude %{_libdir}/%{namever}/libvtkmetaio.so
%exclude %{_libdir}/%{namever}/libvtkNetCDF.so
%exclude %{_libdir}/%{namever}/libvtkParallelPythonD.so
%exclude %{_libdir}/%{namever}/libvtkParallel.so
%exclude %{_libdir}/%{namever}/libvtkproj4.so
%exclude %{_libdir}/%{namever}/libvtkPythonCore.so
%exclude %{_libdir}/%{namever}/libvtkRenderingPythonD.so
%exclude %{_libdir}/%{namever}/libvtkRendering.so
%exclude %{_libdir}/%{namever}/libvtksqlite.so
%exclude %{_libdir}/%{namever}/libvtksys.so
%exclude %{_libdir}/%{namever}/libvtkverdict.so
%exclude %{_libdir}/%{namever}/libvtkViewsPythonD.so
%exclude %{_libdir}/%{namever}/libvtkViews.so
%exclude %{_libdir}/%{namever}/libvtkVolumeRenderingPythonD.so
%exclude %{_libdir}/%{namever}/libvtkVolumeRendering.so
%exclude %{_libdir}/%{namever}/libvtkWidgetsPythonD.so
%exclude %{_libdir}/%{namever}/libvtkWidgets.so
%exclude %{_libdir}/%{namever}/CMake
%doc %{_docdir}/%{namever}
%doc %{_mandir}/man3/*.3*

#-----------------------------------------------------------------------
%package	devel
Summary:	Development files for ParaView
Group:		Sciences/Other
Requires:	%{name} = %{version}-%{release}
Requires:	python-vtk
%if %{with mpi}
%rename		paraview-devel-mpi
%endif

%description	devel
%{summary}.

%files		devel
%defattr(-,root,root,-)
%{_bindir}/kwProcessXML
%{_bindir}/vtkWrapClientServer
%{_includedir}/%{namever}
%{_includedir}/paraview
%{_libdir}/%{namever}/*.cmake
%{_libdir}/%{namever}/libCosmo.so
%{_libdir}/%{namever}/libMapReduceMPI.so
%{_libdir}/%{namever}/libQVTK.so
%{_libdir}/%{namever}/libVPIC.so
%{_libdir}/%{namever}/libvtkalglib.so
%{_libdir}/%{namever}/libvtkChartsPythonD.so
%{_libdir}/%{namever}/libvtkCharts.so
%{_libdir}/%{namever}/libvtkCommonPythonD.so
%{_libdir}/%{namever}/libvtkCommon.so
%{_libdir}/%{namever}/libvtkDICOMParser.so
%{_libdir}/%{namever}/libvtkexoIIc.so
%{_libdir}/%{namever}/libvtkFilteringPythonD.so
%{_libdir}/%{namever}/libvtkFiltering.so
%{_libdir}/%{namever}/libvtkftgl.so
%{_libdir}/%{namever}/libvtkGenericFilteringPythonD.so
%{_libdir}/%{namever}/libvtkGenericFiltering.so
%{_libdir}/%{namever}/libvtkGeovisPythonD.so
%{_libdir}/%{namever}/libvtkGeovis.so
%{_libdir}/%{namever}/libvtkGraphicsPythonD.so
%{_libdir}/%{namever}/libvtkHybridPythonD.so
%{_libdir}/%{namever}/libvtkHybrid.so
%{_libdir}/%{namever}/libvtkImagingPythonD.so
%{_libdir}/%{namever}/libvtkImaging.so
%{_libdir}/%{namever}/libvtkInfovisPythonD.so
%{_libdir}/%{namever}/libvtkInfovis.so
%{_libdir}/%{namever}/libvtkIOPythonD.so
%{_libdir}/%{namever}/libvtkIO.so
%{_libdir}/%{namever}/libvtkmetaio.so
%{_libdir}/%{namever}/libvtkNetCDF.so
%{_libdir}/%{namever}/libvtkParallelPythonD.so
%{_libdir}/%{namever}/libvtkParallel.so
%{_libdir}/%{namever}/libvtkproj4.so
%{_libdir}/%{namever}/libvtkPythonCore.so
%{_libdir}/%{namever}/libvtkRenderingPythonD.so
%{_libdir}/%{namever}/libvtkRendering.so
%{_libdir}/%{namever}/libvtksqlite.so
%{_libdir}/%{namever}/libvtksys.so
%{_libdir}/%{namever}/libvtkverdict.so
%{_libdir}/%{namever}/libvtkViewsPythonD.so
%{_libdir}/%{namever}/libvtkViews.so
%{_libdir}/%{namever}/libvtkVolumeRenderingPythonD.so
%{_libdir}/%{namever}/libvtkVolumeRendering.so
%{_libdir}/%{namever}/libvtkWidgetsPythonD.so
%{_libdir}/%{namever}/libvtkWidgets.so
%{_libdir}/%{namever}/CMake

#-----------------------------------------------------------------------
%package        data
Summary:        Data files for ParaView
Group:          Sciences/Other
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description    data
%{summary}.

%files		data
%defattr(-,root,root,-)
%{_iconsdir}/paraview.png
%{_liconsdir}/paraview.png
%{_miconsdir}/paraview.png
%{_datadir}/mime/packages/paraview.xml
%{_datadir}/%{namever}
%{_datadir}/paraview

#-----------------------------------------------------------------------
%prep
%setup -q -n ParaView-%{version} -a1
mv ParaViewData-%{version}/* .

%patch0 -p1
%patch1 -p1
%patch2 -p1

#-----------------------------------------------------------------------
%build
export CC='gcc'
%if %{with mpi}
export CXX='mpic++'
%else
export CXX='g++'
%endif
export MAKE='make'
export CFLAGS="%{optflags} -DH5_USE_16_API"
export CXXFLAGS="%{optflags} -DH5_USE_16_API"
# Do not use any option not available to "ccmake .." (using "t" to toggle
# advanced options allowed) or it will not respect at least thne
# PARAVIEW_INSTALL_DEVELOPMENT option.
# Most commonly one wants to customize the PV_INSTALL_XXX_DIR options
# but that does not work (it ignores and uses /usr/local); just move files
# around after they are installed, search&replace installed file contents,
# etc.
%cmake									\
	-DBUILD_DOCUMENTATION:BOOL=ON					\
	-DBUILD_EXAMPLES:BOOL=ON					\
	-DBUILD_TESTING:BOOL=OFF					\
	-DCMAKE_CXX_COMPILER=:FILEPATH=$CXX				\
	-DCMAKE_CXX_FLAGS="%{optflags}"					\
	-DCMAKE_C_COMPILER:FILEPATH=$CC					\
	-DCMAKE_C_FLAGS="%{optflags}"					\
	-DPARAVIEW_DATA_ROOT:PATH=%{_datadir}				\
	-DPARAVIEW_BUILD_QT_GUI:BOOL=ON					\
	-DPARAVIEW_ENABLE_PYTHON:BOOL=ON				\
	-DPARAVIEW_INSTALL_DEVELOPMENT:BOOL=ON				\
	-DPARAVIEW_INSTALL_THIRD_PARTY_LIBRARIES:BOOL=OFF		\
%if %{with mpi}
	-DPARAVIEW_USE_MPI:BOOL=ON					\
%else
	-DPARAVIEW_USE_MPI:BOOL=OFF					\
%endif
	-DPYTHON_INCLUDE_PATH:PATH=%{python_include_path}		\
	-DPYTHON_LIBRARY:FILEPATH=%{python_library}			\
	-DQT_INCLUDE_DIR:FILEPATH=%{qt_dir}/include			\
	-DQT_MOC_EXECUTABLE:FILEPATH=%{qt_dir}/bin/moc			\
	-DQT_QMAKE_EXECUTABLE:FILEPATH=%{qt_dir}/bin/qmake		\
	-DQT_UIC_EXECUTABLE:FILEPATH=%{qt_dir}/bin/uic			\
	-DQT_UIC3_EXECUTABLE:FILEPATH=%{qt_dir}/bin/uic3		\
	-DTCL_LIBRARY:PATH=tcl						\
	-DTK_LIBRARY:PATH=tk						\
	-DVTK_INSTALL_QT_PLUGIN_DIR:STRING=%{qt_designer_plugins_dir}	\
	-DVTK_OPENGL_HAS_OSMESA:BOOL=OFF				\
	-DVTK_USE_INFOVIS:BOOL=OFF					\
	-DVTK_USE_SYSTEM_EXPAT:BOOL=ON					\
	-DVTK_USE_SYSTEM_FREETYPE:BOOL=ON				\
	-DVTK_USE_SYSTEM_HDF5:BOOL=ON					\
	-DVTK_USE_SYSTEM_JPEG:BOOL=ON					\
	-DVTK_USE_SYSTEM_LIBXML2:BOOL=ON				\
	-DVTK_USE_SYSTEM_PNG:BOOL=ON					\
	-DVTK_USE_SYSTEM_TIFF:BOOL=ON					\
	-DVTK_USE_SYSTEM_ZLIB:BOOL=ON

# need to load protobuf libraries (also does not build with protobuf 2.4.1)
# http://www.vtk.org/Bug/bug_relationship_graph.php?bug_id=12718&graph=dependency
LD_LIBRARY_PATH=$PWD/bin \
%make

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{_bindir}

# Fix permissions
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -print0 | xargs -0 chmod -x

# Create some needed directories
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_datadir}/mime/packages
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_liconsdir}
install -m644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages
install -m644 %{SOURCE3} ./paraview-logo.png

# Build icons
convert paraview-logo.png -resize 48x48+0+0! -transparent white %{buildroot}%{_liconsdir}/paraview.png
convert paraview-logo.png -resize 32x32+0+0! -transparent white %{buildroot}%{_iconsdir}/paraview.png
convert paraview-logo.png -resize 16x16+0+0! -transparent white %{buildroot}%{_miconsdir}/paraview.png

%ifarch x86_64 ppc64
perl -pi  -e 's|/lib/|/%{_lib}/|g'					\
    `find build -name \*-forward.c`
%endif

%makeinstall_std -C build

# vtk-devel
rm -f %{buildroot}%{_bindir}/vtkWrap*
# vtk-test-suite
rm -f %{buildroot}%{_bindir}/vtkEncodeString

for bin in paraview pvbatch pvdataserver pvpython pvrenderserver pvserver smTestDriver; do
    rm -f %{buildroot}%{_bindir}/$bin
    ln -sf %{_libdir}/%{namever}/$bin %{buildroot}%{_bindir}/$bin
done
cp build/CMake/tmp/pvblot %{buildroot}%{_bindir}
cp build/bin/vtkWrapClientServer %{buildroot}%{_bindir}

# ld.conf.d file
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/paraview > %{buildroot}%{_sysconfdir}/ld.so.conf.d/paraview-%{_arch}.conf

# Python Path
install -d %{buildroot}%{py_platsitedir}
cat > %{buildroot}%{py_platsitedir}/paraview.pth << EOF
%{_libdir}/%{namever}
%{_libdir}/%{namever}/site-packages
%{py_puresitedir}/vtk
EOF

# Create desktop file
cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=ParaView Viewer
GenericName=ParaView Data Viewer
Comment=ParaView allows viewing of large data sets
Type=Application
Terminal=false
Icon=paraview
MimeType=application/x-paraview;
Categories=Graphics;Science;Math;Qt;
Exec=paraview
EOF

desktop-file-install --vendor=""			\
    --dir %{buildroot}%{_datadir}/applications/		\
    %{name}.desktop

mkdir -p %{buildroot}%{_datadir}/%{namever}
cp -fpar Baseline Data %{buildroot}%{_datadir}/%{namever}

%ifarch x86_64 ppc64
mv %{buildroot}%{_prefix}/lib/* %{buildroot}%{_libdir}
%endif

pushd %{buildroot}%{_prefix}
    ln -sf %{namever} %{_lib}/paraview
    %ifarch x86_64 ppc64
    perl -pi -e 's|/lib/|/%{_lib}/|g;'			\
	%{_lib}/%{namever}/*.cmake			\
	%{_lib}/%{namever}/CMake/*.cmake
    %endif
    ln -sf %{namever} include/paraview
    if [ -e share/doc/paraview ]; then
	mv share/doc/paraview/* share/doc/%{namever}
	rm -fr share/doc/paraview
    fi
    ln -sf %{namever} share/paraview
popd
