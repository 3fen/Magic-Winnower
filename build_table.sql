create table cardEssentials(
       cardname char(255),
       cmc int(32),
       color char(1),
       manacost char(255),
       type char(255),
       subtype char(255),
);


create table cardReals(
       cardname char(255),
       artist char(255),
       foil   int(1),
       set    char(255),
       idx    int(10),
       lang   char(255),
);


create table cardsets(
       fullname		char(255),
       abbreviation	char(10),
       totalnum		int(32),
       block		char(10),
       releasedate	date,
       description	char(1024),
);


create table artists(
       name	char(255),
       nation	char(255),
);
