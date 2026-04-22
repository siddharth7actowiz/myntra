@echo off

taskkill /FI "WINDOWTITLE eq Terminal 1" /F
taskkill /FI "WINDOWTITLE eq Terminal 2" /F
taskkill /FI "WINDOWTITLE eq Terminal 3" /F
taskkill /FI "WINDOWTITLE eq Terminal 4" /F