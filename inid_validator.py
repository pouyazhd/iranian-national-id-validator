"""laus deo
Iranian National ID validator 
"""
from dataclasses import dataclass
from random import choice
from random import randint


@dataclass(frozen=True)
class CityCodes:
    """codes of cities in Iran"""

    id_codes = """169
170
149-150
171
168
136-137-138
545
505
636
164-165
172
623
506
519
154-155
567
173
159-160
604
***
274-275
295
637
292
492
289
677
294
493
279-280
288
284-285
638
291
640
293
675
282-283
286-287
296-297
290
***
400-401
404-405
397
398-399
647
502
584
402-403
392-393
395-396
386-387
***
503
444
551
447
561
445
718
083
446
448
552
543
442-443
***
051
052-053
058
055
617
057
618
059-060
061-062
544
056
571
593
***
667
348
586
338-339
343-344
346
337
554
469
537
345
470
341-342
***
483-484
557
418
416-417
412-413
592
612
613
406-407
421
598
419
385
420
528
213-214
205-206
498
568
711
217-218
221
582
483
625
576
578
227
208-209
225
577
712
215-216
626
627
579
713
499
222
219-220
500-501
***
623
497
223
689
487
226
224
486
211-212
628
202-203
531
488
***
261
273
630
264
518
631
258-259
570
265
268-269
653
517
569
267
262-263
593
266
693
271-272
694
270
516
***
333-334
691
323-322
595
395
641
596
336
335
496
337
324-325
394
330
332
331
***
687
422-423
599
600
688
424-425
426
550
697
***
384
377-378
558
385
646
375-376
372-373
379-380
383
674
381-382
676
***
722
542
312-313
317
310-311
302-303
583
321
382
304-305
536
605
308-309
306-307
319
313-314
606
320
698
298-299
535
315-316
318
607
608
***
508
538
728
509
438-439
580
590
559
588
431-432
***
037-038
702
***
240-241
670
648
252
678
253
649
513
546
671
246-247
654
548
547
655
248-249
253
514
665
673
228-229-230
679
256-257
244-245
681
723
236-237
683
656
250-251
515
242 – 243
238-239
657
255
***
684
700
642
457
456
458-459
460
530
520
***
358-359
682
703
364-365
371
701
720
366-367
704
361-362
369-370
635
668
533
705
699
669
725
597
611
525
***
181
527
585
685
663
192-193
174-175
183-184
481
706
194-195
185-186
182
199-200
198
662
190-191
692
189
707
526
187-188
729
730
196-197
661
680
***
643
562
572
74
644
072-073
069-070
521
573
522
724
76
77
650
574
078-079
81
84
651
086-087
089-090
553
91
092-093-094
97
98
96
105-106
***
63
067-068
75
591
82
635
524
***
468
465
461-462
467
632
555
633
629
466
696
***
721
064-065
523
652
719
716
85
88
563
***
529
353
349-350
355
609
351-352
354
732
357
532
610
356
***
556
658
001-002-003-004-005-006 007-008
11
20
25
15
43
666
489
044-045
048-049
490-491
695
659
031-032
664
717
041-042
***
471-472
***
454
581
449-450
616
534
455
451
726
634
453
727
452
***
145-146
731
690
601
504
163
714
715
566
166-167
161-162
686
603
***
619
118
127-128-129
620
621
549
564
575
113-114
122
540
660
120
512
510-511
119
115
112
110-111
125-126
565
121
116-117
541
622
124
108-109
123
428 – 427
507
158
615
152 – 153"""

    @property
    def city_codes(self) -> str:
        """clean starting code of natioanl IDs string

        Returns:
            str: _description_
        """
        codes = self.id_codes.replace("-", "\n")
        codes = codes.replace("***\n", "")
        codes = codes.translate({ord(" "): None})
        codes = codes.split("\n")
        return codes

    @property
    def selected_city_code(self) -> str:
        """randomly select a city code to start generating a valid code

        Returns:
            str: code of random selected city.
        """
        return choice(self.city_codes) + choice(["0", "1"])


class IranianNatioanlID:
    """check and generate Iranian national ID"""

    def __init__(self) -> None:
        self.init_codes = CityCodes()

    @staticmethod
    def validate_string(national_id: str) -> bool:
        """check if input string is totaly numeric and has 10 digits or not.

        Args:
            national_id (str): input ID number in string.
        Raises:
            ValueError: National ID should has 10 digits
            ValueError: National ID is not alpha numeric

        Returns:
            (bool): result of initial checks
        """
        if len(national_id) != 10:
            raise ValueError("National ID should has 10 digits")

        elif not national_id.isnumeric():
            raise ValueError("National ID is not alpha numeric.")
        else:
            return True

    @staticmethod
    def calculate_checksum(national_code):
        """calculate check sum of

        Args:
            national_code (str): _description_

        Returns:
            str: _description_
        """
        checksum_value = 0
        for loc, digit in enumerate(reversed(national_code)):
            checksum_value += int(digit) * (loc + 2)

        last_digit = checksum_value % 11
        if last_digit >= 2:
            last_digit = abs(11 - last_digit)

        return str(last_digit)

    def validation_check(self, national_id: str = None):
        """check if ID code is vlaid or not

        Args:
            national_id (str): input ID number

        Returns:
            bool: result of validation check.
        """
        id_validation = False
        self.validate_string(national_id)

        check_sum = self.calculate_checksum(national_id[:-1])

        if check_sum == national_id[-1]:
            id_validation = True

        return id_validation

    @property
    def new_id(self)->str:
        """generate new ID

        Raises:
            ValueError: generated national ID is not valid.

        Returns:
            (str): generated ID
        """
        national = self.init_codes.selected_city_code
        for _ in range(9 - len(national)):
            national += str(randint(0, 9))
        national += self.calculate_checksum(national)

        try:
            if self.validation_check(national) is True:
                return national
        except:
            raise ValueError("Some error happned during generating national ID.")
