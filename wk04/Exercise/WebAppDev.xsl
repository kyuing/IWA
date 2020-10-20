<?xml version="1.0" encoding="UTF-8" ?>
<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:output method="html" doctype-public="XSLT-compat" omit-xml-declaration="yes" encoding="UTF-8" indent="yes" />


 <!-- <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
</xsl:transform> -->

    <xsl:template match="/">
      <hmtl>
        <head>
          <title>Exercise</title>
        </head>
        <h2>Modules this semester:</h2>
        <xsl:apply-templates select="//name"/>
        <h2>Modules with a Terminal Exam:</h2>
    	<xsl:apply-templates select="//exam"/>
      </hmtl>
    </xsl:template>

    <xsl:template match="name">
        <xsl:value-of select="."/><br/>
    </xsl:template>
    
    <xsl:template match="exam">
        <xsl:value-of select="../name"/><br/>
    </xsl:template>

</xsl:transform>
