function sendEmail() {
   try {
    var ss = SpreadsheetApp.getActive();

    var name = "Urunler";
    var url = "https://docs.google.com/feeds/download/spreadsheets/Export?key=" + ss.getId() + "&exportFormat=xlsx";

    var params = {
      method      : "get",
      headers     : {"Authorization": "Bearer " + ScriptApp.getOAuthToken()},
      muteHttpExceptions: true
    };

    var blob = UrlFetchApp.fetch(url, params).getBlob();

    blob.setName( name + ".xlsx");

    MailApp.sendEmail("tor3sercan@gmail.com", "Rapor Hakkinda", "Rapor Icin Eke bakabilirsiniz", {attachments: [blob]});

  } catch (error) {
    Logger.log(error.toString());
  }
}


1a1da53hBBBRMzjqWhxSETPW821DdYhmUGVmg0KfEGBw