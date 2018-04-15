USE [Arkadium]
GO

/****** Object:  Table [dbo].[tbl_main]    Script Date: 16.04.2018 2:19:30 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
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
