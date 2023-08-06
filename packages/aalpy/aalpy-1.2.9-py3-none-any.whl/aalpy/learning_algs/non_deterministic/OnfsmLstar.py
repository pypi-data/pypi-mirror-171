import time

from aalpy.base import SUL, Oracle
from aalpy.learning_algs.non_deterministic.OnfsmObservationTable import NonDetObservationTable
from aalpy.learning_algs.non_deterministic.TraceTree import SULWrapper
from aalpy.utils.HelperFunctions import print_learning_info, print_observation_table, \
    get_available_oracles_and_err_msg, all_suffixes

print_options = [0, 1, 2, 3]

available_oracles, available_oracles_error_msg = get_available_oracles_and_err_msg()


def run_non_det_Lstar(alphabet: list, sul: SUL, eq_oracle: Oracle, n_sampling=1,
                      max_learning_rounds=None, custom_oracle=False, return_data=False, print_level=2, ):
    """
    Based on ''Learning Finite State Models of Observable Nondeterministic Systems in a Testing Context '' from Fakih
    et al. Relies on the all-weather assumption. (By sampling we will obtain all possible non-deterministic outputs.
    With table-shrinking we mitigate the undesired consequences of the all-weather assumption.

    Args:

        alphabet: input alphabet

        sul: system under learning

        eq_oracle: equivalence oracle

        n_sampling: number of times that each cell has to be updated. If this number is to low, all-weather condition
            will not hold and learning will not converge to the correct model. (Default value = 50)

        max_learning_rounds: if max_learning_rounds is reached, learning will stop (Default value = None)

        custom_oracle: if True, warning about oracle type will be removed and custom oracle can be used

        return_data: if True, map containing all information like number of queries... will be returned
            (Default value = False)

        print_level: 0 - None, 1 - just results, 2 - current round and hypothesis size, 3 - educational/debug
            (Default value = 2)

    Returns:
        learned ONFSM

    """

    if not custom_oracle and type(eq_oracle) not in available_oracles:
        raise SystemExit(available_oracles_error_msg)

    start_time = time.time()
    eq_query_time = 0
    learning_rounds = 0
    hypothesis = None

    sul = SULWrapper(sul)
    eq_oracle.sul = sul

    observation_table = NonDetObservationTable(alphabet, sul, n_sampling)

    # We fist query the initial row. Then based on output in its cells, we generate new rows in the extended S set,
    # and then we perform membership/input queries for them.
    observation_table.update_obs_table()
    observation_table.get_extended_S()
    observation_table.update_obs_table()

    # Keep track of last counterexample and last hypothesis size
    # With this data we can check if the extension of the E set lead to state increase
    last_cex = None

    while True:
        learning_rounds += 1
        if max_learning_rounds and learning_rounds - 1 == max_learning_rounds:
            break

        # Close observation table
        row_to_close = observation_table.get_row_to_close()
        while row_to_close is not None:
            # First we add new rows to the extended S set. They are added based on the values in the cells of the
            # rows that is to be closed. Once those rows are created, they are populated and closedness is checked
            # once again.
            observation_table.update_obs_table()
            observation_table.clean_obs_table()
            row_to_close = observation_table.get_row_to_close()

        # Generate hypothesis
        hypothesis = observation_table.gen_hypothesis()

        # Cex has been successfully processed
        if counterexample_not_valid(hypothesis, last_cex):

            # Find counterexample
            if print_level > 1:
                print(f'Hypothesis {learning_rounds}: {len(hypothesis.states)} states.')

            if print_level == 3:
                print_observation_table(observation_table, 'non-det')

            eq_query_start = time.time()
            cex = eq_oracle.find_cex(hypothesis)
            last_cex = cex
            eq_query_time += time.time() - eq_query_start
        else:
            cex = last_cex

        # If no counterexample is found, return the hypothesis
        if cex is None:
            break

        if print_level == 3:
            print('Counterexample', cex)

        # Process counterexample -> Extract suffixes to be added to E set
        # cex_suffixes = non_det_longest_prefix_cex_processing(observation_table, cex)
        cex_suffixes = all_suffixes(cex[0])
        for suffix in cex_suffixes:
            if suffix not in observation_table.E:
                observation_table.E.append(suffix)
                break

        # Add all suffixes to the E set and ask membership/input queries.
        observation_table.update_obs_table()

    total_time = round(time.time() - start_time, 2)
    eq_query_time = round(eq_query_time, 2)
    learning_time = round(total_time - eq_query_time, 2)
    info = {
        'learning_rounds': learning_rounds,
        'automaton_size': len(hypothesis.states),
        'queries_learning': sul.num_queries,
        'steps_learning': sul.num_steps,
        'queries_eq_oracle': eq_oracle.num_queries,
        'steps_eq_oracle': eq_oracle.num_steps,
        'learning_time': learning_time,
        'eq_oracle_time': eq_query_time,
        'total_time': total_time
    }

    if print_level > 0:
        print_learning_info(info)

    if return_data:
        return hypothesis, info

    return hypothesis


def counterexample_not_valid(hypothesis, cex):
    if cex is None:
        return True
    hypothesis.reset_to_initial()
    for i, o in zip(cex[0], cex[1]):
        out = hypothesis.step_to(i, o)
        if out is None:
            return False
    return True
