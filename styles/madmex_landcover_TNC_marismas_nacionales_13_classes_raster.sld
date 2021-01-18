<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.0.0" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>Marismas Nacionales 13 clases</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="values">
              <sld:ColorMapEntry label="Manglar y Peten" quantity="8" color="#fb061b"/>
              <sld:ColorMapEntry label="Selva Baja Caducifolia Subcaducifolia y Matorral Subtropical" quantity="11" color="#e43fc6"/>
              <sld:ColorMapEntry label="Vegetacion Halofila Hidrofila" quantity="26" color="#1c9048"/>
              <sld:ColorMapEntry label="Pastizales" quantity="27" color="#f2f2cf"/>
              <sld:ColorMapEntry label="Tierras Agricolas" quantity="28" color="#f7ff05"/>
              <sld:ColorMapEntry label="Urbano y Construido" quantity="29" color="#4d1009"/>
              <sld:ColorMapEntry label="Suelo Desnudo" quantity="30" color="#c9cdcc"/>
              <sld:ColorMapEntry label="Agua" quantity="31" color="#011eff"/>
              <sld:ColorMapEntry label="Manglar y Peten, arbustivo" quantity="80" color="#f97681"/>
              <sld:ColorMapEntry label="Selva Baja Caducifolia Subcaducifolia y Matorral Subtropical, arbustivo" quantity="110" color="#f891e4"/>
              <sld:ColorMapEntry label="Pastizales, desprovisto" quantity="111" color="#dadcb4"/>
              <sld:ColorMapEntry label="Tierras agricolas, desprovisto" quantity="112" color="#f4f899"/>
              <sld:ColorMapEntry label="Agua, periodica" quantity="113" color="#4257f4"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
