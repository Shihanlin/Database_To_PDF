#!/usr/bin/env python
#coding=utf-8
import platform

class Settings():
	def __init__(self):
		self.os_type = platform.uname()[0]
		self.doc_header="某某某某项目"
		self.oracleUserName="sys"
		self.oracleUserPassword="Wisedu#123"
		self.oracleServiceName="172.16.9.73:1521/zhfwdb"
		self.sql_test=" select t.tablespace_name Tablespace_name,\
        substr(t.contents, 1, 1) Type,\
        round(d.tbs_size/1024/1024,2) Used_MB,\
        round(d.tbs_maxsize/1024/1024,2) MaxSize_MB,\
        round(nvl(d.tbs_maxsize-d.tbs_size,0)/1024/1024,2) FreeSpace_MB,\
        decode(d.tbs_maxsize, 0, 0, round(d.tbs_size/d.tbs_maxsize,4)*100)||'%' usage\
		from\
 		( select SUM(bytes) tbs_size,\
        SUM(decode(sign(maxbytes - bytes), -1, bytes, maxbytes)) tbs_maxsize, tablespace_name tablespace\
    	from ( select nvl(bytes, 0) bytes, nvl(maxbytes, 0) maxbytes, tablespace_name\
    	from dba_data_files\
    	union all\
    	select nvl(bytes, 0) bytes, nvl(maxbytes, 0) maxbytes, tablespace_name\
    	from dba_temp_files\
    	)\
    	group by tablespace_name\
    	) d,\
    	dba_tablespaces t\
    	where t.tablespace_name = d.tablespace(+)\
    	order by 1"
