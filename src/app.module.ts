import { Module } from '@nestjs/common';
import { cacheModule } from './cache/cache.module';

@Module({
  imports: [cacheModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
