import cv2
import datetime

if __name__ == "__main__":
    try:

        cap = cv2.VideoCapture('Sample_Video_1.mp4')
        ret, frame1 = cap.read()

        while True:

            _, frame1 = cap.read()
            _, frame2 = cap.read()

            cv2.rectangle(frame1, (100, 132), (400, 350), (0, 0, 255), 2)
            cv2.rectangle(frame2, (100, 132), (400, 350), (0, 0, 255), 2)

            frame1_original = frame1
            frame2_original = frame2

            frame1_a = frame1[132:350, 100:400]
            frame2_a = frame2[132:350, 100:400]

            cv2.rectangle(frame1, (566, 75), (796, 299), (0, 200, 255), 2)
            cv2.rectangle(frame2, (566, 75), (796, 299), (0, 200, 255), 2)
            frame1_b = frame1[75:299, 566:796]
            frame2_b = frame2[75:299, 566:796]

            cv2.rectangle(frame1, (794, 357), (1204, 162), (150, 150, 200), 2)
            cv2.rectangle(frame2, (794, 357), (1204, 162), (150, 150, 200), 2)
            frame1_c = frame1[162:357, 794:1204]
            frame2_c = frame2[162:357, 794:1204]

            cv2.rectangle(frame1, (77, 656), (414, 298), (255, 0, 255), 2)
            cv2.rectangle(frame2, (77, 656), (414, 298), (255, 0, 255), 2)
            frame1_d = frame1[298:656, 77:414]
            frame2_d = frame2[298:656, 77:414]

            diff_a = cv2.absdiff(frame1_a, frame2_a)
            diff_b = cv2.absdiff(frame1_b, frame2_b)
            diff_c = cv2.absdiff(frame1_c, frame2_c)
            diff_d = cv2.absdiff(frame1_d, frame2_d)

            gray_a = cv2.cvtColor(diff_a, cv2.COLOR_BGR2GRAY)
            gray_b = cv2.cvtColor(diff_b, cv2.COLOR_BGR2GRAY)
            gray_c = cv2.cvtColor(diff_c, cv2.COLOR_BGR2GRAY)
            gray_d = cv2.cvtColor(diff_d, cv2.COLOR_BGR2GRAY)

            blur_a = cv2.GaussianBlur(gray_a, (5, 5), 0)
            blur_b = cv2.GaussianBlur(gray_b, (5, 5), 0)
            blur_c = cv2.GaussianBlur(gray_c, (5, 5), 0)
            blur_d = cv2.GaussianBlur(gray_d, (5, 5), 0)

            _, thresh_a = cv2.threshold(blur_a, 20, 255, cv2.THRESH_BINARY)
            _, thresh_b = cv2.threshold(blur_b, 20, 255, cv2.THRESH_BINARY)
            _, thresh_c = cv2.threshold(blur_c, 20, 255, cv2.THRESH_BINARY)
            _, thresh_d = cv2.threshold(blur_d, 20, 255, cv2.THRESH_BINARY)

            dilated_a = cv2.dilate(thresh_a, None, iterations=3)
            dilated_b = cv2.dilate(thresh_b, None, iterations=3)
            dilated_c = cv2.dilate(thresh_c, None, iterations=3)
            dilated_d = cv2.dilate(thresh_d, None, iterations=3)

            contours_a, _ = cv2.findContours(dilated_a, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours_b, _ = cv2.findContours(dilated_b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours_c, _ = cv2.findContours(dilated_c, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours_d, _ = cv2.findContours(dilated_d, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour_a in contours_a:
                (x_a, y_a, w_a, h_a) = cv2.boundingRect(contour_a)

                if cv2.contourArea(contour_a) > 1 :
                    cv2.rectangle(frame1_a, (x_a, y_a), (x_a + w_a, y_a + h_a), (0, 255, 0), 2)
                    cv2.putText(frame1_a, "Status: {}".format('Movement Detected'),
                                (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 3)

                else:
                    continue

            for contour_b in contours_b:
                (x_b, y_b, w_b, h_b) = cv2.boundingRect(contour_b)

                if cv2.contourArea(contour_b) > 0.5:
                    cv2.rectangle(frame1_b, (x_b, y_b), (x_b + w_b, y_b + h_b), (0, 255, 0), 2)
                    cv2.putText(frame1_b, "Status: {}".format('Movement Detected'),
                                (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 3)

                else:
                    continue

            for contour_c in contours_c:
                (x_c, y_c, w_c, h_c) = cv2.boundingRect(contour_c)

                if cv2.contourArea(contour_c) > 0.5 :
                    cv2.rectangle(frame1_c, (x_c, y_c), (x_c + w_c, y_c + h_c), (0, 255, 0), 2)
                    cv2.putText(frame1_c, "Status: {}".format('Movement Detected'),
                                (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 3)

                else:
                    continue

            for contour_d in contours_d:
                (x_d, y_d, w_d, h_d) = cv2.boundingRect(contour_d)

                if cv2.contourArea(contour_d) > 0.5 :
                    cv2.rectangle(frame1_d, (x_d, y_d), (x_d + w_d, y_d + h_d), (0, 255, 0), 2)
                    cv2.putText(frame1_d, "Status: {}".format('Movement Detected'),
                                (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 3)
                else:
                    continue
            cv2.putText(frame1_b, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S:%p"), (10, frame1_b.shape[0] - 10)
                        , cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 200, 255), 1)
            cv2.putText(frame1_a, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S:%p"),
                        (10, frame1_a.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.putText(frame1_c, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S:%p"), (10, frame1_c.shape[0] - 10)
                        , cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 200), 1)
            cv2.putText(frame1_d, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S:%p"), (10, frame1_d.shape[0] - 10)
                        , cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 0, 255), 1)

            cv2.imshow('Motion Detection', frame1_original)
            frame1 = frame2
            ret, frame2 = cap.read()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        print("Video Has Ended")
        exit(0)
    except Exception as ex:
        print(ex)

else:
    print("This file must be run as \"main\"")
