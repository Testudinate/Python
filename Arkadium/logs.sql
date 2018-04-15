/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [round_name]
      ,[boxer_name]
      ,[country_name]
      ,[result]
  FROM [Arkadium].[dbo].[tbl_stage_data]

  delete from [Arkadium].[dbo].[tbl_stage_data]

  insert into [Arkadium].[dbo].[tbl_country] (country_id,country_name)
   select ROW_NUMBER() OVER(ORDER BY sub.country_name asc) rw 
        , sub.country_name
     from ( select distinct country_name as country_name
             from [Arkadium].[dbo].[tbl_stage_data] ) as sub;

select * from [Arkadium].[dbo].[tbl_country]

delete from  [Arkadium].[dbo].[tbl_country]


  insert into [Arkadium].[dbo].[tbl_round] (round_id,round_name)
   select ROW_NUMBER() OVER(ORDER BY sub.round_name asc) rw 
        , sub.round_name
     from ( select distinct round_name as round_name
             from [Arkadium].[dbo].[tbl_stage_data] ) as sub;

select * from [Arkadium].[dbo].[tbl_round]

delete from  [Arkadium].[dbo].[tbl_round]

drop table [Arkadium].[dbo].[tbl_round]
drop table [Arkadium].[dbo].[tbl_country]
drop table [Arkadium].[dbo].[main]

delete from [Arkadium].[dbo].[tbl_main]

select * from [Arkadium].[dbo].[tbl_main]

delete from [Arkadium].[dbo].[tbl_main];

insert into [Arkadium].[dbo].[tbl_main] (boxer_name,result,round_id,country_id) 
select cast(replace(st.boxer_name,'В','') as nvarchar(50))
     , cast(st.result as nvarchar(5))
	 , cast(r.round_id as int)
	 , cast(c.country_id as int)
  from [Arkadium].[dbo].[tbl_stage_data] st
  left join [Arkadium].[dbo].[tbl_round] r on r.round_name = st.round_name
  left join [Arkadium].[dbo].[tbl_country] c on c.country_name = st.country_name;


CREATE TABLE [dbo].[tbl_stage_data](
	[round_name] [nvarchar](50) NOT NULL,
	[boxer_name] [nvarchar](50) NOT NULL,
	[country_name] [nvarchar](50) NOT NULL,
	[result] [nvarchar](50) NULL
) ON [PRIMARY]


CREATE TABLE [dbo].[tbl_round](
	[round_id] [int] NOT NULL,
	[round_name] [nvarchar](16) NOT NULL,
 CONSTRAINT [PK_tbl_round] PRIMARY KEY CLUSTERED 
(
	[round_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[tbl_country](
	[country_id] [int] NOT NULL,
	[country_name] [nvarchar](5) NOT NULL,
 CONSTRAINT [PK_tbl_country] PRIMARY KEY CLUSTERED 
(
	[country_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO



CREATE TABLE [dbo].[tbl_main](
	[boxer_name] [nvarchar](32) NOT NULL,
	[result] [nvarchar](5) NULL,
	[country_id] [int] NOT NULL,
	[round_id] [int] NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[tbl_main]  WITH CHECK ADD  CONSTRAINT [FK_tbl_main_tbl_country] FOREIGN KEY([country_id])
REFERENCES [dbo].[tbl_country] ([country_id])
GO

ALTER TABLE [dbo].[tbl_main] CHECK CONSTRAINT [FK_tbl_main_tbl_country]
GO

ALTER TABLE [dbo].[tbl_main]  WITH CHECK ADD  CONSTRAINT [FK_tbl_main_tbl_round] FOREIGN KEY([round_id])
REFERENCES [dbo].[tbl_round] ([round_id])
GO

ALTER TABLE [dbo].[tbl_main] CHECK CONSTRAINT [FK_tbl_main_tbl_round]
GO


