import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PositionService } from '../service/position.service';
import { Position } from '../model/position';

@Component({
  selector: 'app-position-list',
  templateUrl: './position-list.component.html',
  styleUrls: ['./position-list.component.scss', '../app.component.scss'],
})
export class PositionListComponent implements OnInit {
  positions: Position[] = [];
  public title: string = '';

  constructor(
    public positionService: PositionService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe((params) => {
      this.title = params['title'];
      this.positionService
        .getPositions(params['title_id'])
        .subscribe((positions) => (this.positions = positions));
    });
  }
}
