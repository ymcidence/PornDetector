# BadImageFinder

### Requirements 
- python 2.7
- opencv 2.4 (you can take binary from repository)
- tensorflow >=1.14
- flask
- numpy
- pathlib

### Usage
- Firstly run the api: `python ./manage_worse.py`
- The api receives a list of image urls splitted by '|', e.g.
```
url1|url2|url3
```
- It returns a Json with two fields
```
predction [N]: 1--bad image; 0--normal image
preds [N*4]: probability of 0--pron image; 1--bloody image; 2--violent image; 3--normal image 
```
- One is able to send a http request to the api in Java as follows
```java
List<String> imageUrl = ANY URL YOU LIKE;
HttpClient client = HttpClientBuilder.create().build();
String url = "your server ip:6000/hehe/worse_image/";
HttpPost request = new HttpPost(url);
try
{
    StringBuilder mergedUrl = new StringBuilder();
    for (String i : imageUrl) {
        mergedUrl.append(i).append("|");
    }
    String mergedUrlString = mergedUrl.toString();
    Map< String, Object > jsonValues = new HashMap< String, Object >();
    jsonValues.put("urls", mergedUrlString.substring(0, mergedUrlString.length() - 1));
    StringEntity postingString = new StringEntity(jsonValues.toString(), "UTF8");
    postingString.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
    request.setEntity(postingString);
    HttpResponse response = client.execute(request);
    // DO WHATEVER YOU LIKE HERE TO PROCESS THE RESULTS
} catch (Exception e){
    ...
}
```

