import { Injectable } from '@nestjs/common';
import { redis_client } from "./redis_warper/redis_client";
import endPointurl from "./config/appConfig";

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }

  private urlAnalyze = endPointurl.UserUrl;
  async postAnalyze(header,json) {

    const catchRequest = redis_client.getInstance();
    const requestId = JSON.stringify(json)
    
    const value = await catchRequest.get(requestId)
    if(value){
        return  {body:value, responseStatus: 200};
    }else{

        const body = JSON.stringify(json)
        const response = await fetch(this.urlAnalyze, {
          method: 'POST',
          body: body,
          headers: {'content-type':header['content-type']}
        });
    
    if(response.status >= 400){
      return {body: null, responseStatus: response.status, statusText:response.statusText};
    }
    
    const outer_serverResposne = await response.text()
    await catchRequest.set(requestId, outer_serverResposne)
    return {body: outer_serverResposne, responseStatus: 200};

   }
  } 

}
