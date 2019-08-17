import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  titles: string[];

  constructor(){
    this.titles = ['You must be the change you wish to see in the world — Gandhi','Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid — Albert Einstein','A life spent making mistakes is not only more honorable, but more useful than a life spent doing nothing— George Bernhard Shaw','God, grant me the serenity to accept the things I cannot change, the courage to change the things I can, and the wisdom to know the difference — Reinhold Niebuhr', 'Life is never made unbearable by circumstances, but only by lack of meaning and purpose — Viktor Frankl']
  }
}
