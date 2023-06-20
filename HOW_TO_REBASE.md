# How to rebase on top of _Black_

On _Cercis_'s GitHub page, we can see (near the top of the page):

> This branch is \*\* commits ahead of psf:main, \*\* commits behind psf:main.

Whenever we see "behind psf:main", we should rebase to incorporate the newest changes
from _Black_.

Here are the steps to rebase:

## 1. Create a merge commit

Go to GitHub Desktop, and in "History" (hear the top left corner), choose the branch
"upstream/main".

The "Behind" section shows the commits that we are behind _Black_. It should be
non-zero. If it is zero, click the "🔄" button near the top right of the window.

And then click "Create a merge commit" button on the bottom left.

![](./screenshots/how_to_rebase/1.png)

## 2. Resolve merge conflicts

If there are merge conflicts, GitHub Desktop will show a warning. Resolve the conflict
using the tool of your choice.

![](./screenshots/how_to_rebase/2.png)

## 3. Push changes

Then, use GitHub Desktop or your terminal to push the changes.

After pushing, you'll see that "\*\* commits behind psf:main" is gone.

![](./screenshots/how_to_rebase/3.png)
