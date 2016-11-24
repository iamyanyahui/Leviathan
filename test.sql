ALTER DATABASE leviathan DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
alter table table_name convert to character set utf8;

INSERT into location(province,city,county,street) VALUES ('Beijing','Beijing','Haidian','37,Xueyuan Road');
INSERT into location(province,city,county,street) VALUES ('北京','北京','海淀','学院路37号');
INSERT into hospital(name,level,type,information,_createtime,id_location_id)
VALUES ('北航校医','三级甲等','普通','北航医院，人少，学生管报销，速来。','2016/11/24 14:35',1);
INSERT into department(name,id_hospital_id) VALUES('外科',1);
INSERT INTO doctor(name, level, speciality, information,careertime, gender, age, _createtime)
VALUES ('王大海','主任医师','外科','十年从医',10,'男',55,'2016/11/24 14:35');
