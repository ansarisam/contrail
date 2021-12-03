<?xml version="1.0" encoding="ISO-8859-1"?>
<isl debug="true" loop="1" offscreen="true" sleep="60.0minutes">
  <bundle clear="true" file="${islpath}/General.xidv" wait="true"/>
  <center north="56.2" south="33.7" east="-89.4" west="-139.8"/>
  <movie file="${islpath}/testContrails0${time:yyyy_MM_dd_hh_mm}.gif" imagedir="${islpath}" imagetemplate="image0_%time%" imagesuffix="png">
    <resize width="1200"/>
  </movie>
  <center north="51.7" south="36.1" east="-57.7" west="-92.9"/>
  <movie file="${islpath}/testContrails1${time:yyyy_MM_dd_hh_mm}.gif" imagedir="${islpath}" imagetemplate="image1_%time%" imagesuffix="png">
    <resize width="1200"/>
  </movie>
  <center north="37.4" south="21.9" east="-69.9" west="-98.1"/>
  <movie file="${islpath}/testContrails2${time:yyyy_MM_dd_hh_mm}.gif" imagedir="${islpath}" imagetemplate="image2_%time%" imagesuffix="png">
    <resize width="1200"/>
  </movie>
  <center north="41.7" south="21.6" east="-87.9" west="-124.8"/>
  <movie file="${islpath}/testContrails3${time:yyyy_MM_dd_hh_mm}.gif" imagedir="${islpath}" imagetemplate="image3_%time%" imagesuffix="png">
    <resize width="1200"/>
  </movie>
</isl>
