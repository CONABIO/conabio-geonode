<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>mex_RE_2015_8_clases</sld:Name>
            <sld:Title/>
            <sld:FeatureTypeStyle>
                <sld:Name/>
                <sld:Rule>
                    <sld:RasterSymbolizer>
                        <sld:Geometry>
                            <ogc:PropertyName>grid</ogc:PropertyName>
                        </sld:Geometry>
                        <sld:Opacity>1</sld:Opacity>
                        <sld:ColorMap>
                            <sld:ColorMapEntry color="#ffffff" label="Sin datos" opacity="0.0" quantity="0"/>
                            <sld:ColorMapEntry color="#4d642d" label="Bosque Templado" opacity="1.0" quantity="1"/>
                            <sld:ColorMapEntry color="#4cb974" label="Selva Perennifolia, Subperennifolia, Caducifolia y Subcaducifolia" opacity="1.0" quantity="2"/>
                            <sld:ColorMapEntry color="#e59f26" label="Matorral" opacity="1.0" quantity="3"/>
                            <sld:ColorMapEntry color="#e0b762" label="Vegetación menor y Pastizales" opacity="1.0" quantity="4"/>
                            <sld:ColorMapEntry color="#9c9877" label="Tierras Agrícolas" opacity="1.0" quantity="5"/>
                            <sld:ColorMapEntry color="#b4b8bc" label="Urbano y Construido" opacity="1.0" quantity="6"/>
                            <sld:ColorMapEntry color="#3f2f21" label="Suelo Desnudo" opacity="1.0" quantity="7"/>
                            <sld:ColorMapEntry color="#2eccfa" label="Agua" opacity="1.0" quantity="8"/>
                            <sld:ColorMapEntry color="#000000" label="Nubes" opacity="1.0" quantity="9"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>

