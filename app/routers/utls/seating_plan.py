def generate_seating_plan(theater_seating, booked_seats, headcount, selected_row):
    # Get the total number of seats in the selected row
    total_seats_in_row = theater_seating[selected_row]

    if len(booked_seats) == 0:
        # No seats were booked in the row
        # Use centred seats to generate an array of seats with a size of headcount as the seating plan
        center = total_seats_in_row // 2
        seating_plan_start = center - (headcount // 2)
        if seating_plan_start >= 0:
            seating_plan_end = seating_plan_start + headcount
            seating_plan = list(range(seating_plan_start, seating_plan_end))
            return seating_plan
        else:
            return []

    else:
        # Center seats were allocated
        smallest_booked_seat = min(booked_seats)
        largest_booked_seat = max(booked_seats)
        seats_available_left = smallest_booked_seat
        seats_available_right = total_seats_in_row - largest_booked_seat - 1

        left_start_seat = smallest_booked_seat - headcount
        left_end_seat = left_start_seat + headcount - 1
        right_start_seat = largest_booked_seat + 1
        right_end_seat = largest_booked_seat + headcount
        if seats_available_left >= seats_available_right:
            # prioritize left side
            if left_start_seat >= 0:
                seating_plan = list(range(left_start_seat, left_end_seat + 1))
                return seating_plan
            else:
                # can't use single side
                seating_plan = list(range(0, left_end_seat + 1)) \
                               + list(range(right_start_seat, right_start_seat + abs(left_start_seat)))
                return seating_plan

        if seats_available_left < seats_available_right:
            # prioritize right side
            if right_end_seat < total_seats_in_row:
                seating_plan = list(range(right_start_seat, right_end_seat + 1))
                return seating_plan
            else:
                # can't use single side
                new_left_start_seat = left_end_seat - (right_end_seat - total_seats_in_row)
                seating_plan = list(range(new_left_start_seat, left_end_seat + 1)) \
                               + list(range(right_start_seat, total_seats_in_row + 1))
                return seating_plan

    return []
