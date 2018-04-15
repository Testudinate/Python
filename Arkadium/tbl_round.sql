USE [Arkadium]
GO

/****** Object:  Table [dbo].[tbl_round]    Script Date: 16.04.2018 2:20:51 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tbl_round](
	[round_id] [int] NOT NULL,
	[round_name] [nvarchar](16) NOT NULL,
 CONSTRAINT [PK_tbl_round] PRIMARY KEY CLUSTERED 
(
	[round_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO


