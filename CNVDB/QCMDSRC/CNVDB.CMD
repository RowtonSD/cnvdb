             CMD        PROMPT('Import / Extract DB2 Table')

            PARM KWD(FROMTYPE) TYPE(*CHAR) LEN(3) RSTD(*YES) +
                 DFT(XLS) VALUES(('XLS') ('CSV') ('SQL') ('DB2')) +
                 PROMPT('Source type')
            PARM KWD(FROMFILE) TYPE(*CHAR) LEN(255) PROMPT('File being imported')
            PARM KWD(FROMHOST) TYPE(*CHAR) LEN(20) DFT('LOCALHOST') PROMPT('Source hostname')
            PARM KWD(FROMUSER) TYPE(*CHAR) LEN(20) PROMPT('Source username')
            PARM KWD(FROMPASS) TYPE(*CHAR) LEN(20) PROMPT('Source password')
            PARM KWD(FROMDB) TYPE(*CHAR) LEN(20) PROMPT('Source database')
            PARM KWD(FROMTBL) TYPE(*CHAR) LEN(20) PROMPT('Source table')
            PARM KWD(FROMRDB) TYPE(*CHAR) LEN(10) PROMPT('Source RDB entry')
            PARM KWD(DESTTYPE) TYPE(*CHAR) LEN(3) RSTD(*YES) +
                 DFT(XLS) VALUES(('XLS') ('CSV') ('SQL') ('DB2')) +
                 PROMPT('Destination type')
            PARM KWD(DESTFILE) TYPE(*CHAR) LEN(255) PROMPT('Destination file')
            PARM KWD(DESTHOST) TYPE(*CHAR) LEN(20) DFT('LOCALHOST') PROMPT('Destination hostname')
            PARM KWD(DESTUSER) TYPE(*CHAR) LEN(20) PROMPT('Destination username')
            PARM KWD(DESTPASS) TYPE(*CHAR) LEN(20) PROMPT('Destination password')
            PARM KWD(DESTDB) TYPE(*CHAR) LEN(20) PROMPT('Destination database')
            PARM KWD(DESTTBL) TYPE(*CHAR) LEN(20) PROMPT('Destination table')
            PARM KWD(DESTRDB) TYPE(*CHAR) LEN(10) PROMPT('Destination RDB entry')

