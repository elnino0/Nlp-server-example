import { Controller, Post,Body, Headers, HttpException, Param} from '@nestjs/common';
import { AppServiceCatch } from './app.service';


interface SendDetailsDTO {
  service: string;
}

@Controller()
export class AppController {
  constructor(private readonly appService: AppServiceCatch) {}
  
  @Post(":service")
  async analyze(@Param() params: SendDetailsDTO, @Headers() headers, @Body() message){
    console.log(params)
    const responseFromAnalyze = await this.appService.postAnalyze(params.service, headers, message);
    if (responseFromAnalyze.responseStatus == 200){
        return responseFromAnalyze.body;
    }else{
      throw new HttpException(responseFromAnalyze.statusText, responseFromAnalyze.responseStatus);
    }

  }
}
