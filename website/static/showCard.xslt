<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
    <xsl:output method="html" encoding="UTF-8"/>
    <xsl:template match="/">
        <html>
            <head>
                <title>Cartas de Magic</title>
            </head>
            <body>
                <h1>Cartas de Magic</h1>
                <div>
                    <xsl:for-each select="Cartas/Carta">
                        <div>
                            <h2><xsl:value-of select="Nombre"/></h2>
                            <p><strong>Maná:</strong> <xsl:value-of select="Mana"/>
                               <strong> Tipo:</strong> <xsl:value-of select="Tipo"/>
                               <strong> Descripción:</strong> <xsl:value-of select="Descripcion"/>
                            </p>
                        </div>
                    </xsl:for-each>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>