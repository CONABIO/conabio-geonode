<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" maxScale="0" minScale="1e+08" version="3.6.3-Noosa" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property value="false" key="WMSBackgroundLayer"/>
    <property value="false" key="WMSPublishDataSourceUrl"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="Value" key="identify/format"/>
  </customproperties>
  <pipe>
    <rasterrenderer type="paletted" band="1" opacity="1" alphaBand="-1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <colorPalette>
        <paletteEntry value="8" alpha="255" label="Manglar y Peten" color="#fb061b"/>
        <paletteEntry value="11" alpha="255" label="Selva Baja Caducifolia Subcaducifolia y Matorral Subtropical" color="#e43fc6"/>
        <paletteEntry value="26" alpha="255" label="Vegetacion Halofila Hidrofila" color="#1c9048"/>
        <paletteEntry value="27" alpha="255" label="Pastizales" color="#f2f2cf"/>
        <paletteEntry value="28" alpha="255" label="Tierras Agricolas" color="#f7ff05"/>
        <paletteEntry value="29" alpha="255" label="Urbano y Construido" color="#4d1009"/>
        <paletteEntry value="31" alpha="255" label="Agua" color="#011eff"/>
        <paletteEntry value="80" alpha="255" label="Manglar y Peten, arbustivo" color="#f97681"/>
        <paletteEntry value="110" alpha="255" label="Selva Baja Caducifolia Subcaducifolia y Matorral Subtropical, arbustivo" color="#f891e4"/>
        <paletteEntry value="270" alpha="255" label="Pastizales, desprovisto" color="#dadcb4"/>
        <paletteEntry value="280" alpha="255" label="Tierras acricolas, desprovisto" color="#f4f899"/>
        <paletteEntry value="310" alpha="255" label="Agua, periodica" color="#4257f4"/>
        <paletteEntry value="30" alpha="255" label="Suelo Desnudo" color="#c9cdcc"/>
      </colorPalette>
      <colorramp type="randomcolors" name="[source]"/>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation saturation="0" grayscaleMode="0" colorizeGreen="128" colorizeBlue="128" colorizeStrength="100" colorizeOn="0" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
