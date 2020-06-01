import { Component, OnInit, Input } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { Position } from '../../model/position';

@Component({
  selector: 'app-position',
  templateUrl: './position.component.html',
  styleUrls: ['./position.component.scss'],
})
export class PositionComponent implements OnInit {
  @Input() position: Position;
  constructor(protected _sanitizer: DomSanitizer) {}

  ngOnInit(): void {}

  safeHtml(html: string) {
    return this._sanitizer.bypassSecurityTrustHtml(html);
  }

  handleApply(): void {
    alert(`You applied for ${this.position.title}`);
  }
}
