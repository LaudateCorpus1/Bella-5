'''
Unit test suite for the :py:mod:`tdparse.contexts` module.
'''
from unittest import TestCase


from tdparse.contexts import right_context
from tdparse.contexts import left_context
from tdparse.contexts import _context

class TestContexts(TestCase):
    '''
    Contains the following functions:
    '''
    single_context = [{'text':'This is a fake news article that is to represent a Tweet!!!!',
                       'target':'news article',
                       'spans':[[15, 27]]},
                      {'text':'I had a great day however I did not get much work done',
                       'target':'day',
                       'spans':[[14, 17]]},
                      {'text':'I cycled in today and it was ok as it was not raining.',
                       'target':'cycled',
                       'spans':[[2, 8]]}]
    multi_contexts = [{'text':'This is a fake news article that is to represent a '\
                       'Tweet!!!! and it was an awful News Article I think.',
                       'target':'news article',
                       'spans':[[15, 27], [81, 93]]},
                      {'text':'I had a great Day however I did not get much '\
                       'work done in the day',
                       'target':'day',
                       'spans':[[14, 17], [62, 65]]}]
    def test_context(self):
        '''
        Tests :py:func:`tdparse.contexts._context`
        '''
        with self.assertRaises(ValueError, msg='Should only accept left and right '\
                               'context words for parameters'):
            _context(self.single_context[0], 'itself')

    def test_left_context(self):
        '''
        Tests :py:func:`tdparse.contexts.left_context`
        '''

        single_left = [['This is a fake '], ['I had a great '], ['I ']]
        for index, test_context in enumerate(self.single_context):
            test_text = test_context['text']
            test_target = test_context['target']
            correct_context = single_left[index]
            left_string = left_context(test_context, inc_target=False)
            msg = 'Cannot get the left context of target {} text {} which should be {}'\
                  ' and not {}'.format(test_target, test_text, correct_context, left_string)
            self.assertEqual(correct_context, left_string, msg=msg)
        # Handle including targets
        single_left = [['This is a fake news article'], ['I had a great day'],
                       ['I cycled']]
        for index, test_context in enumerate(self.single_context):
            test_text = test_context['text']
            test_target = test_context['target']
            correct_context = single_left[index]
            left_string = left_context(test_context, inc_target=True)
            msg = 'Cannot get the left context of target {} text {} including the '\
                  'target which should be {} and not {}'\
                  .format(test_target, test_text, correct_context, left_string)
            self.assertEqual(correct_context, left_string, msg=msg)

        multi_left = [['This is a fake ', 'This is a fake news article that is to'\
                       ' represent a Tweet!!!! and it was an awful '],
                      ['I had a great ', 'I had a great Day however I did not get '\
                        'much work done in the ']]
        for index, test_context in enumerate(self.multi_contexts):
            test_text = test_context['text']
            test_target = test_context['target']
            correct_context = multi_left[index]
            left_string = left_context(test_context, inc_target=False)
            msg = 'Cannot get the left context of target {} text {} which should be {}'\
                  ' and not {}'.format(test_target, test_text, correct_context, left_string)
            self.assertEqual(correct_context, left_string, msg=msg)
        # Handle including targets
        multi_left = [['This is a fake news article', 'This is a fake news article '\
                       'that is to represent a Tweet!!!! and it was an awful News Article'],
                      ['I had a great Day', 'I had a great Day however I did not get '\
                        'much work done in the day']]
        for index, test_context in enumerate(self.multi_contexts):
            test_text = test_context['text']
            test_target = test_context['target']
            correct_context = multi_left[index]
            left_string = left_context(test_context, inc_target=True)
            msg = 'Cannot get the left context of target {} text {} including the '\
                  'target which should be {} and not {}'\
                  .format(test_target, test_text, correct_context, left_string)
            self.assertEqual(correct_context, left_string, msg=msg)


    def test_right_context(self):
        '''
        Tests :py:func:`tdparse.contexts.right_context`
        '''

        single_right = [[' that is to represent a Tweet!!!!'],
                        [' however I did not get much work done'],
                        [' in today and it was ok as it was not raining.']]
        for index, test_context in enumerate(self.single_context):
            test_text = test_context['text']
            test_target = test_context['target']
            correct_context = single_right[index]
            right_string = right_context(test_context, inc_target=False)
            msg = 'Cannot get the right context of target {} text {} '\
                  'which should be {} and not {}'\
                  .format(test_target, test_text, correct_context, right_string)
            self.assertEqual(correct_context, right_string, msg='Cannot get the '\
                             'right context of target {} text {} which should be {}'\
                             ' and not {}'.format(test_target, test_text,
                                                  correct_context, right_string))
        # Handle including targets
        single_right = [['news article that is to represent a Tweet!!!!'],
                        ['day however I did not get much work done'],
                        ['cycled in today and it was ok as it was not raining.']]
        for index, test_context in enumerate(self.single_context):
            test_text = test_context['text']
            test_target = test_context['target']
            correct_context = single_right[index]
            right_string = right_context(test_context, inc_target=True)
            msg = 'Cannot get the right context of target {} text {} including the '\
                  'target which should be {} and not {}'\
                  .format(test_target, test_text, correct_context, right_string)
            self.assertEqual(correct_context, right_string, msg=msg)

        multi_right = [[' that is to represent a Tweet!!!! and it was an awful News'\
                       ' Article I think.', ' I think.'],
                       [' however I did not get much work done in the day', '']]
        for index, test_context in enumerate(self.multi_contexts):
            test_text = test_context['text']
            test_target = test_context['target']
            correct_context = multi_right[index]
            right_string = right_context(test_context, inc_target=False)
            msg = 'Cannot get the right context of target {} text {} which should be {}'\
                  ' and not {}'\
                  .format(test_target, test_text, correct_context, right_string)
            self.assertEqual(correct_context, right_string, msg=msg)
        # Handle including targets
        multi_right = [['news article that is to represent a Tweet!!!! and it was'\
                        ' an awful News Article I think.', 'News Article I think.'],
                       ['Day however I did not get much work done in the day', 'day']]
        for index, test_context in enumerate(self.multi_contexts):
            test_text = test_context['text']
            test_target = test_context['target']
            correct_context = multi_right[index]
            right_string = right_context(test_context, inc_target=True)
            msg = 'Cannot get the right context of target {} text {} including the '\
                  'target which should be {} and not {}'\
                  .format(test_target, test_text, correct_context, right_string)
            self.assertEqual(correct_context, right_string, msg=msg)
