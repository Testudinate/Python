USE [Arkadium]
GO

/****** Object:  Table [dbo].[tbl_stage_data]    Script Date: 16.04.2018 2:21:22 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tbl_stage_data](
	[round_name] [nvarchar](50) NOT NULL,
	[boxer_name] [nvarchar](50) NOT NULL,
	[country_name] [nvarchar](50) NOT NULL,
	[result] [nvarchar](50) NULL
) ON [PRIMARY]
GO


