#pragma once

extern "C" bool ConvertXmlToDae ( const char* pszGameBaseFolderPath, const char* pszXmlFilePath, const char* pszDaeFilePath, char* pszError, int iMaxErrorSize );
extern "C" bool ConvertDaeToXml ( const char* pszGameBaseFolderPath, const char* pszDaeFilePath, const char* pszXmlFilePath, char* pszError, int iMaxErrorSize );
