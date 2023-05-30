import { Module, MiddlewareConsumer, NestModule, RequestMethod} from '@nestjs/common';
import { AppController } from './cache.controller';
import { AppServiceCatch } from './cache.service';

@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppServiceCatch],
})

export class cacheModule implements NestModule {
  public configure(consumer: MiddlewareConsumer) {
    consumer.apply().forRoutes({path: ':service', method: RequestMethod.POST});
  }
}
