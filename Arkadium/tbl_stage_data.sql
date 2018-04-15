USE [Arkadium]
GO

/****** Object:  Table [dbo].[tbl_stage_data]    Script Date: 15.04.2018 22:12:08 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tbl_stage_data](
	[round_name] [varchar](50) NOT NULL,
	[boxer_name] [varchar](50) NOT NULL,
	[country_name] [varchar](50) NOT NULL,
	[result] [varchar](50) NULL
) ON [PRIMARY]
GO
